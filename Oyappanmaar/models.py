from django.db import models

class Credentials(models.Model):
    name = models.CharField(max_length=32)
    username = models.CharField(max_length=8)
    password = models.CharField(max_length=32)

