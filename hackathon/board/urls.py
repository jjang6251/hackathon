from django.urls import path
from .views import *

app_name = 'board'
urlpatterns = [
    path('list/', board_list, name='board_list'),
    path('write/', board_write, name='board_write'),
    path('update/', board_update, name='board_update'),
    path('detail/', board_detail, name='board_detail'),
    path('modify/<int:pk>/', board_modify, name='board_modify'),
]




