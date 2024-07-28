from django.db import models

class Record(models.Model):
    photo = models.ImageField(upload_to='img/')
    created_date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    provience = models.CharField(max_length=100)
    country = models.CharField(max_length=100)


    def __str__(self) -> str:
        return self.first_name + "  " + self.last_name
