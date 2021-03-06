from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_picture',default='man.png')
    bio=  models.CharField(max_length=300,null=True,blank=True)
    hide_email=  models.BooleanField(default=True)
    full_name=  models.CharField(max_length=30,null=True,blank=True)
    loaction=  models.CharField(max_length=100,null=True,blank=True)
    email= models.EmailField(max_length=60)
    #, unique=True
    date_joined	= models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return str(self.user)

    # def get_absolute_url(self):
    #    return reverse("profiles:my_profile", kwargs={"pk": self.pk })

    # def get_posts_no(self):
    #     return self.post_set.all().count() 

    # def get_all_authors_posts(self):
    #     return self.post_set.all()

    # def get_all_profiles(self):
    #     return self.profile_set.all()



@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()




