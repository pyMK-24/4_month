from django.shortcuts import render,redirect,get_object_or_404
from . import models,forms

def todo_list(request):
    if request.method == 'GET':
        query = models.TodoModel.objects.all()
        context_object_name = {
            'todo_lst': query
        }
        return render(request,template_name='todo/todo_list.html',context=context_object_name)

def create_todo(request):
    if request.method == 'POST':
        form = forms.TodoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('todo_lst')
    else:
        form = forms.TodoForm()
    return render(request, template_name='todo/create_todo.html',context={'form': form})

def delete_todo_view(request,id):
    todo_id = get_object_or_404(models.TodoModel,id=id)
    todo_id.delete()
    return redirect('todo_lst')

def update_todo_view(request,id):
    todo_id = get_object_or_404(models.TodoModel, id=id)
    if request.method == 'POST':
        form = forms.TodoForm(request.POST, instance=todo_id)
        if form.is_valid():
            form.save()
            return redirect('todo_lst')
    else:
        form = forms.TodoForm(instance=todo_id)
    return render(request, template_name='todo/update_todo.html',context={'form': form,
                                                                          'todo_id': todo_id,
                                                                          })




