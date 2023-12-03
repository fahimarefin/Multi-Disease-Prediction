from django.db import models
from datetime import datetime

class Contact(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    description = models.TextField()
    date = models.DateField(default=datetime.now)  # You can use any default date you prefer

    def __str__(self):
        return self.name
