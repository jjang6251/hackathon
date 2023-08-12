from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()

class Board(models.Model):
    board_image = models.ImageField(null=True, upload_to='images/')
    board_content = models.TextField(verbose_name='내용')
    money = models.TextField(verbose_name='가격')
    title = models.CharField(max_length=64, verbose_name='글 제목')
    board_category = models.CharField(max_length=32, default='카테고리 등록해주세요', verbose_name='카테고리')
    write_dttm = models.DateTimeField(auto_now_add=True, verbose_name='글 작성시간')
    update_dttm = models.DateTimeField(auto_now=True, verbose_name='마지막 수정일')
    view_count = models.IntegerField(default=0, verbose_name='조회수')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Board'
        verbose_name = '게시판'
        verbose_name_plural = '게시판'


