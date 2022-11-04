from django.db import models

class Allowed(models.Model):
    roll = models.CharField(max_length=8)
    
class Credentials(models.Model):
    person = models.CharField(max_length=32)
    username = models.CharField(max_length=8)
    password = models.CharField(max_length=32)
    
class Note(models.Model):
    user = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    notes = models.CharField(max_length=100)
    l = models.IntegerField()

class NotePublic(models.Model):
    user = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    notes = models.CharField(max_length=32)
    l = models.IntegerField()
    