from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class CustomUser(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    add=models.CharField(max_length=30, blank=True)
    dob=models.CharField(max_length=20)
    phone_no=models.CharField(max_length=12)
    class Meta:
        db_table="customuser"

@receiver(post_save, sender=User)
def create_customuser(sender, instance, created, **kwargs):
    if created:
        CustomUser.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_customuser(sender, instance, **kwargs):
    instance.customuser.save()
    

class Users(models.Model):
    name = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    price = models.CharField(max_length=10)

    class Meta:
        db_table = "users"


