from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="todo_index"),
    path("edit/<int:pk>/", views.edit_task, name="edit_task"),
    path("delete/<int:pk>/", views.delete_task, name="delete_task"),
    path("complete_task/<int:pk>/", views.complete_task, name="complete_task"),
]
