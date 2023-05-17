from django.db import models

# Create your models here.
class blog(models.Model):
    title=models.CharField(max_length=250)
    txet=models.CharField(max_length=1000)
    date=models.DateField()
    def __str__(self):
        return self.title

