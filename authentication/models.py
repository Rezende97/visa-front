from django.db import models

class Management(models.Model):
   
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    class Meta:
        db_table = 'management'
