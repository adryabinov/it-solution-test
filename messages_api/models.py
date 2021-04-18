from django.db import models

# Create your models here.
class MessageFromSpace(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    read = models.BooleanField(auto_created=False)

    def __str__(self):
        return f'{self.date}  {self.text}'

    def mk_unread(self):
        self.read = False
