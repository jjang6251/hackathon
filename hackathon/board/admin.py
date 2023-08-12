# from django.contrib import admin
# from .models import Board
# from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import Board

class BoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'board_nickname', 'board_location', 'board_number', 'board_image', 'board_content', 'money', 'title', 'board_write_dttm', 'board_update_dttm', 'view_count')  # 목록에서 보여줄 필드 설정
    list_filter = ('board_category', )  # 필터 기능을 사용할 필드 설정
    search_fields = ('title', 'content', 'board_nickname', 'board_location')  # 검색 기능을 사용할 필드 설정
    ordering = ('-id',)  # 기본 정렬 순서 설정

    fieldsets = (
        ('글 정보', {
            'fields': ('image', 'title', ' board_content', 'board_category')
        }),
        ('작성자 정보', {
            'classes': ('collapse',),
            'fields': ('board_nickname', 'board_location', 'board_number')
        }),
    )

    def save_model(self, request, obj, form, change):
        if not obj.writer:
            obj.writer = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Board, BoardAdmin)

