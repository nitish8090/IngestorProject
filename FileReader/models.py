from django.db import models


class HotFile(models.Model):
    """ The files which are added to the hot folder """

    path = models.FileField()

