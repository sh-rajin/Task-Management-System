from django.db import models
from category.models import Category


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ManyToManyField(Category)
    assign_date = models.DateField()
    is_complete = models.BooleanField(default=False)


    def __str__(self):
        return self.title


