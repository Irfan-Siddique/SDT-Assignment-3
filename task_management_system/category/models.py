from django.db import models
# from task.models import Task

# Create your models here.
class Category(models.Model):
    categoryName=models.CharField(max_length=30)
    # task=models.ManyToManyField(Task, related_name="categories")

    def __str__(self):
        return self.categoryName