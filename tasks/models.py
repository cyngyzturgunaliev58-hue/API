
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200, verbose_name="Тапшырма")
    description = models.TextField(verbose_name="Тактама")
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False, verbose_name="Аткарылды")

    def __str__(self):
        return self.title