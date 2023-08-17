from django.db import models
from django.contrib.auth.models import AbstractUser,User

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