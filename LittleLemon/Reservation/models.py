from django.db import models

# Create your models here.
class Booking(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        indexes = [
            models.Index(fields=['price']),
        ]
        
        
class Registration(models.Model):
    username = models.CharField(max_length=200, db_index=True)
    url = models.CharField(max_length=100, db_index=True)
    email = models.CharField(max_length=20, db_index=True)
    group = models.CharField(max_length=100, db_index=True)
