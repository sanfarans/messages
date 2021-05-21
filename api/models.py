from django.db import models


class Message(models.Model):
    text = models.CharField(max_length=160)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.text
