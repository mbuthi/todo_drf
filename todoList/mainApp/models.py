from django.db import models

# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True)
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)
    is_completed = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.title