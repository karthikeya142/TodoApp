from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Task
from .Forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView

# Create your views here.
#the way in which this view works is that we have extracted all the objects and then we have simply
#passed those particular objects to this particular template.
#So we had accomplished this particular task using this view. #you can see, this view is actually a function based view.
# this particular case, this same functionality can actually be applied or actually be performed
#using a class based generic view, which is called as a list view.
def index(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        priority = request.POST.get('priority', '0')  # Default to None if not provided
        date     = request.POST.get('date','')
        task = Task(name=name, priority=priority, date=date)
        task.save()
        return redirect('/')
        form = TaskForm(request.POST)
        if form.is_valid():
            # Process the data
            return redirect('success_url')
        else:
            # Handle invalid form
            return render(request, 'myapp/index.html', {'form': form})
    else:
        form = TodoForm()
    task_list = Task.objects.all()
    return render(request, 'myapp/index.html', {'task_list': task_list, 'form': form})

def update(request,id):
    task =Task.objects.get(id=id)
    form =TodoForm(request.POST or None, request.FILES, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'myapp/edit.html', {'form':form,'task':task})

def delete(request,taskid):
    taskid = Task.objects.get(id=taskid)
    if request.method == "POST":
        taskid.delete()
        return redirect('/')
    return render(request, 'myapp/delete.html',{'taskid':taskid})

# Whenever you want to display a list of items, what you simply do is that you go ahead and create list view
# create a list view, first of all you need to import list view.
#nce we have the list view, we can now actually go ahead and create an actual list view here.
# as I earlier mentioned, a list view is a class based generic view.

class TaskListView(ListView):
    model= Task
    template_name = 'myapp/index.html'
    context_object_name = 'task_list'
class TaskDetailView(DetailView):
    model=Task
    template_name = 'myapp/detail.html'
    context_object_name = 'task'

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'myapp/update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')
    def get_success_url(self):
        return reverse_lazy('cbvdetail', kwargs={'pk':self.object.id})

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'myapp.delete.html'
    success_url =  reverse_lazy('cbvindex')