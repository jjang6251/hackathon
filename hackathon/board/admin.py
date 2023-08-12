# from django.contrib import admin
# from .models import Board
# from django_summernote.admin import SummernoteModelAdmin
from django.contrib import admin
from .models import Board

class BoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'board_name', 'user_nickname', 'user_location', 'writer', 'view_count', 'user_ph_number')  # 목록에서 보여줄 필드 설정
    list_filter = ('board_name', )  # 필터 기능을 사용할 필드 설정
    search_fields = ('title', 'content', 'user_nickname', 'user_location', 'writer__username')  # 검색 기능을 사용할 필드 설정
    ordering = ('-id',)  # 기본 정렬 순서 설정

    fieldsets = (
        ('글 정보', {
            'fields': ('board_name', 'title', 'content', 'image')
        }),
        ('작성자 정보', {
            'classes': ('collapse',),
            'fields': ('writer', 'user_nickname', 'user_location', 'user_ph_number')
        }),
    )

    def save_model(self, request, obj, form, change):
        if not obj.writer:
            obj.writer = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Board, BoardAdmin)

