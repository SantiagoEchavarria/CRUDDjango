from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from .forms import TaskForm
from .models import Task
from django.utils import timezone
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'GET':
        print('Enviando formulario')
        return render(request, 'signup.html', {
            'form': UserCreationForm()
        })

    else:
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # Verificar si las contraseñas coinciden
        if password1 != password2:
            return HttpResponse('Las contraseñas no coinciden')

        # Verificar si el usuario ya existe
        if User.objects.filter(username=username).exists():
            return HttpResponse('El usuario ya existe')

        # Crear el usuario si todo está bien
        user = User.objects.create_user(username=username, password=password1)

        # Autenticar al usuario antes de iniciar sesión
        user = authenticate(username=username, password=password1)

        if user:
            login(request, user)  # Ahora sí funciona correctamente

        return redirect('tasks')

@login_required
def tasks(request):
    #Listar las tareas
    #tasks = Task.objects.all()
    tasks = Task.objects.filter(usuario=request.user, fechaCompletada__isnull=True).order_by('-fechaCompletada')
    return render(request, 'tasks.html', {'tasks': tasks
                                          }) 
@login_required 
def tasks_completed(request):
    #Listar las tareas
    #tasks = Task.objects.all()
    tasks = Task.objects.filter(usuario=request.user, fechaCompletada__isnull=False)
    return render(request, 'tasks.html', {'tasks': tasks
                                          }) 

@login_required
def create_tasks(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {
            'form': TaskForm
        })
    else:
        try:
            form = TaskForm(request.POST)
            nuevaTarea = form.save(commit=False)
            nuevaTarea.usuario = request.user
            nuevaTarea.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'create_task.html', {
            'form': TaskForm,
            'error': "Datos invalidos"
            })

@login_required       
def complete_task(request, task_id):
       task = get_object_or_404(Task, pk=task_id, usuario= request.user)
       if request.method=="POST":
           task.fechaCompletada = timezone.now()
           task.save()
           return redirect('tasks')

@login_required
def delete_task(request, task_id):
       task = get_object_or_404(Task, pk=task_id, usuario= request.user)
       if request.method=="POST":
           task.delete()
           return redirect('tasks')
       
@login_required
def task_detail(request, task_id):
    if request.method == 'GET':
        #task=Task.objects.get(pk=task_id)
        task = get_object_or_404(Task,pk=task_id, usuario=request.user)
        form = TaskForm(instance=task)
        return render(request, 'task_detail.html', {'task':task,
                                                    'form':form})
    else:
        try:
            task = get_object_or_404(Task,pk=task_id, usuario=request.user)
            form =TaskForm(request.POST, instance=task)
            form.save()
            return redirect('tasks')
        except ValueError:
            return render(request, 'task_detail.html', {'task':task,
                                                    'form':form,
                                                    'error': 'Error actualizando el formulario'})
        
@login_required
def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET': 
        return render(request,'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request,'signin.html', {
                'form': AuthenticationForm,
                'error': 'Username or password is incorrect'
        })
        else:
            login(request, user)
            return redirect('tasks')
        

