from django.db import models
from shortuuid.django_fields import ShortUUIDField

# Create your models here.


class Customers(models.Model):
    name = models.CharField(max_length=200, null=True)
    surname = models.CharField(max_length=200, null=True,)
    email = models.EmailField(max_length=200, null=True, blank=True)
    phone_number = models.CharField(max_length=13, null=True,)
    address = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    id = ShortUUIDField(
        length=4,
        max_length=4,
        prefix="SE",
        alphabet="ABCDEFGHJKLMNOPQRWSVXTUZY1234567890",
        primary_key=True,
    )


    def __str__(self):
        return self.name

