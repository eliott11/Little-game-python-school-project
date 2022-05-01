from django.db import models

class Question(models.Model):
    title = models.CharField(max_length = 200)
    description = models.CharField(max_length = 400)