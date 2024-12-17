from django.db import models
from category.models import Category
# Create your models here.

class Task(models.Model):
    taskTitle=models.CharField(max_length=50)
    taskDescription=models.TextField()
    category=models.ManyToManyField(Category,related_name='task')
    is_completed=models.BooleanField(default=False)
    taskAssignDate=models.DateField()

    def __str__(self):
        return self.taskTitle