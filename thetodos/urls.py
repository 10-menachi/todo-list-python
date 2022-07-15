from django.urls import path
from . import views

urlpatterns = [
    path('', views.TodoView.as_view(), name='home'),
    path('add', views.add_todos, name='add_todos'),
    path('delete/<int:todo_id>/', views.delete_todos, name='delete_todos')
]
