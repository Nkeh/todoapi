from django.urls import path
from .views import *

urlpatterns = [
    path('', ListToDo.as_view(), name="todo.list"),
    path('create/', CreateToDo.as_view(), name="todo.new"),
    path('<int:pk>/', DetailToDo.as_view(), name="todo.detail"),
    path('<int:pk>/delete/',DeleteToDo.as_view(), name="todo.delete"),
]
