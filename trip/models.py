from django.db import models

# Create your models here.
class destination(models.Model):
    img=models.ImageField(upload_to='pics')
    name=models.CharField(max_length=100)
    desc=models.TextField()
    price=models.IntegerField()
    offer=models.BooleanField(default=False)

    