from django import forms
from .models import Board

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['board_image', 'board_nickname', 'title', 'money', 'board_content', 'board_location_si', 'board_location_gu', 'board_location_dong', 'board_number']
        widgets = {
            'board_image': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
            'board_nickname': forms.Textarea(),
            'title': forms.Textarea(),
            'money': forms.Textarea(),
            'board_content': forms.Textarea(),
            'board_location_si': forms.Textarea(),
            'board_location_gu': forms.Textarea(),
            'board_location_dong': forms.Textarea(),
            'board_number': forms.Textarea(),
        }
