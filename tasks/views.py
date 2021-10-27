from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator

from .models import Task
from .forms import TaskForm

#Real aplication

def taskList(request):
    findAllTasks = Task.objects.all().order_by('-created_at')
    search = request.GET.get('search')
    if search:
        findAllTasks = findAllTasks.filter(title__icontains=search)

    paginator = Paginator(findAllTasks, 5)
    page = request.GET.get('page')
    tasks = paginator.get_page(page)
    return render(request, 'tasks/list.html', {'tasks': tasks})

def taskView(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'task': task})

def newTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)

        if form.is_valid():
            task = form.save(commit=False)
            task.done = 'doing'
            task.save()
            messages.info(request, 'Tarefa adcionada com sucesso')
            return redirect('/')
    else:
        form = TaskForm()
        return render(request, 'tasks/addTask.html', {'form': form})

def editTask(request, id):
    task = get_object_or_404(Task, pk=id)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)

        if form.is_valid():
            form.save()
            messages.info(request, 'Tarefa atualizada com sucesso')
            return redirect('/')
        else:
            return render(request, 'tasks/edit.html', {'form': form, 'task': task})
    else:
        return render(request, 'tasks/edit.html', {'form': form, 'task': task})

def deleteTask(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()
    messages.info(request, 'Task deletada com sucesso')
    return redirect('/')

#example

def yourName(request, name):
    return render(request, 'tasks/yourName.html', {'name': name})

def helloWorld(request):
    return HttpResponse('Hello world!')