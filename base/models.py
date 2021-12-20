from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="usuarie")#si el user es deleted se borra toda la info
    title = models.CharField(max_length=200, verbose_name="titulo")
    description = models.TextField(null=True, blank=True, verbose_name="descripción")
    complete = models.BooleanField(default=False, verbose_name="hecho")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        #string representation for the model
        return self.title

    class Meta:
        ordering = ['complete']