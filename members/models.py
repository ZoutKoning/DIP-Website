from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Role(models.Model):
    userRole = models.CharField(max_length=7)

    def __str__(self):
        return self.userRole


# ROLES
DRIVER = "driver"
SPONSOR = "sponsor"
ADMIN = "admin"
ROLE_CHOICES = (
    (DRIVER, "driver"),
    (SPONSOR, "sponsor"),
    (ADMIN, "admin"),
)

# SPONSORS
AMAZON = "Amazon"
YOUTUBE = "YouTube"
MICROSOFT = "Microsoft"
NONE = "NONE"
SPONSOR_CHOICES = (
    (AMAZON, "Amazon"),
    (YOUTUBE, "YouTube"),
    (MICROSOFT, "Microsoft"),
    (NONE, "NONE"),
)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, related_name='profile')
    # username = models.CharField(max_length=150, unique=True)
    role = models.CharField(max_length=7, choices=ROLE_CHOICES, default=DRIVER)
    # mySponsors = models.CharField(max_length=9, choices=SPONSOR_CHOICES, default=NONE)
    approved = models.BooleanField('Approved', default=False)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    print(created)
    if created:
        UserProfile.objects.create(user=instance)
        print('created user profile')
    else:
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()
            print('updated')
        except:

            UserProfile.objects.create(user=instance)
            print('Profile did not exist, created one now.')



