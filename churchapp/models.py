from django.db import models

# Create your models here.

class Subsribers(models.Model):  
    first_name = models.CharField(max_length=30)  
    last_name = models.CharField(max_length=30)
    date = models.DateField(max_length=30)
    class Meta:  
        db_table = "subscribers"