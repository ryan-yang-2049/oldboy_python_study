from django.db import models

# Create your models here.

class Role(models.Model):

	title = models.CharField(max_length=32)