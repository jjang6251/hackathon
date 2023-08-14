from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

class Board(models.Model):
    board_nickname = models.CharField(max_length=20, verbose_name='고객 닉네임')
    board_location = models.CharField(max_length=60, verbose_name='고객 위치', default='거래 희망 장소를 입력해주세요')
    board_number = models.CharField(max_length=15, verbose_name='고객님 전화번호')
    board_image = models.ImageField(null=True, upload_to='images/')
    board_content = models.TextField(verbose_name='내용')
    money = models.TextField(verbose_name='심부름 가격')
    title = models.CharField(max_length=64, verbose_name='글 제목')
    board_category = models.CharField(max_length=32, default='카테고리 등록해주세요', verbose_name='카테고리')
    board_write_dttm = models.DateTimeField(auto_now=True, verbose_name='글 작성시간')
    board_update_dttm = models.DateTimeField(auto_now=True, verbose_name='마지막 수정일')
    view_count = models.PositiveIntegerField(default=0, verbose_name='조회수')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Board'
        verbose_name = '게시판'
        verbose_name_plural = '게시판'