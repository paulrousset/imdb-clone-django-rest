from django.db import models


class Content(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    active = models.BooleanField(default=True)

# The __str__ method in Python represents the class objects as a string
    def __str__(self):
        return self.name
