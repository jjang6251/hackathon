from django.forms import ModelForm
from .models import *

class BoardForm(ModelForm):
    class Meta:
        model = Board
        fields = ['image', 'content', 'user_nickname', 'user_location', 'user_ph_number', 'title', 'board_name', 'view_count', 'writer'] 
        # 'write_dttm', 'update_dttm'



