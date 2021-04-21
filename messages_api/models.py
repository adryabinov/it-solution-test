from django.db import models
from django.contrib import admin

# Create your models here.


class MessageFromSpace(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    is_read = models.BooleanField(auto_created=False)

    def serialize(self):
        return {
            'id': self.pk,
            'date': self.date,
            'text': self.text,
            'is_read': self.is_read,
        }

    def __str__(self):
        return f'{self.date}  {self.text}'
