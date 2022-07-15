from django.views.generic import ListView
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Todo
from django.urls import reverse_lazy


# Create your views here.
class TodoView(ListView):
    model = Todo
    template_name = 'main/home.html'
    context_object_name = 'todos'


@csrf_exempt
def add_todos(request):
    todo_text = request.POST["content"]
    Todo.objects.create(text=todo_text)
    return redirect('/')
    reverse_lazy('add_todos')


@csrf_exempt
def delete_todos(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return redirect('/')
