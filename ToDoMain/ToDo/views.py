from django.shortcuts import get_object_or_404, render,redirect
from ToDo.models import Task
# Create your views here.
def Home(request):
    tasks=Task.objects.filter(is_completed=False).order_by('-created_at')
    completed_tasks=Task.objects.filter(is_completed=True) 
    context={
        'tasks':tasks,
        'completed_tasks':completed_tasks
    }
    return render(request, 'home-todo.html', context)
def AddTask(request):
    task=request.POST['task']
    Task.objects.create(task=task)
    return redirect('Home')
def MarkAsDone(request, pk):
    task=Task.objects.get(pk=pk)
    task.is_completed=True
    task.save()
    return redirect('Home')
def MarkAsUndone(request, pk):
    task=get_object_or_404(Task, pk=pk)
    task.is_completed=False
    task.save()
    return redirect('Home')
def EditTask(request, pk):
    get_task=get_object_or_404(Task, pk=pk)
    if request.method=='POST':
        new_task=request.POST['task']
        get_task.task=new_task
        get_task.save()
        return redirect('Home')
    else:
        context={
            'get_task': get_task,
        }
        return render(request, 'EditTask.html', context)
def DeleteTask(request, pk):
    task=get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('Home')