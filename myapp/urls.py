
from django.urls import path
from . import views

urlpatterns = [
    path("", views.TaskView.as_view({'get': 'list'}), name="tasks"),
    path("get/<str:id>", views.getTaskByID, name="getTasks"),
    path("add/", views.createTask, name="createtask"),
    path("edit/<str:id>", views.updateTask, name="edittask"),
    path("delete/<str:id>", views.deleteTask, name="deltask"),
]