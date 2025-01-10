from django.db import models

class Customers(models.Model):
    
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    passaporte = models.TextField(max_length=255)

    class Meta:
        db_table = 'users'

