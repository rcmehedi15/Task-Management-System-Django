from django.shortcuts import render, redirect
from .models import TaskModel
from .forms import TaskForm

def task_list(request):
    tasks = TaskModel.objects.all()
    return render(request, 'task/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'task/task_form.html', {'form': form})

def edit_task(request, task_id):
    task = TaskModel.objects.get(id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'task/task_form.html', {'form': form})

def delete_task(request, task_id):
    task = TaskModel.objects.get(id=task_id)
    task.delete()
    return redirect('task_list')
