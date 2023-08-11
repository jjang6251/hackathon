from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    gender = models.CharField(max_length=5, verbose_name="성별")
    address = models.CharField(max_length=50, verbose_name="사는 거주지 주소")
    resi_num = models.CharField(max_length=30, verbose_name="주민등록번호")
    ph_num = models.CharField(max_length=30, verbose_name="전화번호")
    nickname = models.CharField(max_length=50, verbose_name="닉네임")
    resi_img = models.ImageField(null=True, verbose_name="주민등록증 사진")
    present_img = models.ImageField(null=True, verbose_name="현재 사진")

