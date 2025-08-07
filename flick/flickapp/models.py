from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class adminpanel(models.Model):
   description=models.CharField(max_length=500,null=True)
   title=models.CharField(max_length=100,null=True)
   Image=models.ImageField(upload_to='images/', null=True)
   drive_link = models.URLField(blank=True, null=True)
   action_movie=models.BooleanField(default=False)
   for_kids=models.BooleanField(default=False)
   horror =models.BooleanField(default=False)
   malayalam =models.BooleanField(default=False)
   tamil =models.BooleanField(default=False)
   feelgood=models.BooleanField(default=False)
   family =models.BooleanField(default=False)
   comedy=models.BooleanField(default=False)
   fantasy=models.BooleanField(default=False)
   crime_thriller=models.BooleanField(default=False)
   survival_movie =models.BooleanField(default=False)
   adventure=models.BooleanField(default=False)
   science_fiction=models.BooleanField(default=False)

   def __str__(self):
      return self.title








class Payment1(models.Model):
    username = models.CharField(max_length=100, default="")
    password = models.CharField(max_length=100,)  # Store hashed if possible
    card_number = models.CharField(max_length=19, default="**** **** **** 1234")  # Read-only field in frontend
    cvv = models.CharField(max_length=4)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    subscription_plan = models.CharField(max_length=20, default="100")  # Basic, Standard, Premium
    paid_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} - ₹{self.amount} ({self.subscription_plan})"



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.user.username


