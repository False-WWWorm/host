from django.db import models

class Add(models.Model):
    #title = models.TextField()
    content = models.FileField(upload_to="audio")
