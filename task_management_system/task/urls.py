from django.urls import path
from . import views
urlpatterns = [

    path('add/',views.add_task, name='add_task'),
    path('show_task/',views.show_tasks, name='show_tasks'),
    path('edit/<int:id>',views.edit_task, name='edit_task'),
    path('delete/<int:id>',views.delete_task, name='delete_task'),
]