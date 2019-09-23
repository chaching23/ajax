from django.db import models

class post(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)

