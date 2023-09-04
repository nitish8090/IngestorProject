from django.db import models

class Imagery(models.Model):

    path = models.FileField()