from django.db import models
from django.contrib.auth.models import AbstractUser,User

from django.db.models.signals import post_save
from django.dispatch import receiver

class User(AbstractUser):
    gender = models.CharField(max_length=5, verbose_name="성별")
    address_si = models.CharField(max_length=50, verbose_name="거주지(시)")
    address_gu = models.CharField(max_length=50, verbose_name="거주지(구)")
    address_dong = models.CharField(max_length=50, verbose_name="거주지(동)")
    resi_num = models.CharField(max_length=30, verbose_name="주민등록번호")
    ph_num = models.CharField(max_length=30, verbose_name="전화번호")
    nickname = models.CharField(max_length=50, verbose_name="닉네임")
    resi_img = models.ImageField(null=True, verbose_name="주민등록증 사진", upload_to='users/')
    present_img = models.ImageField(null=True, verbose_name="현재 사진", upload_to='users/')


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    ph_num = models.CharField(max_length=20)
    nickname = models.CharField(max_length=30)

    def __str__(self):
        return self.user.username 

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    try:

        instance.profile.address = instance.address_si + ' ' + instance.address_gu + ' ' + instance.address_dong
        instance.profile.ph_num = instance.ph_num
        instance.profile.nickname = instance.nickname
        instance.profile.save()
    except Profile.DoesNotExist:  # profile이 없는 경우
        Profile.objects.create(user=instance, address=instance.address_si + ' ' + instance.address_gu + ' ' + instance.address_dong, ph_num=instance.ph_num, nickname=instance.nickname)
