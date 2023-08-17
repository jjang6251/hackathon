from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model
from django.forms.models import ModelForm
from .models import Profile, User


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields=['first_name', 'last_name',]
        exclude = ['password', ]

class ProfileForm(forms.ModelForm):
    username = forms.CharField(label="아이디", required=False)
    nickname = forms.CharField(label="닉네임", required=False)
    email = forms.CharField(label="이메일", required=False)
    ph_num = forms.CharField(label="전화번호", required=False)
    address = forms.CharField(label="주소", required=False)
    class Meta:
        model=Profile
        fields = ['nickname', 'email','ph_num','address_si','address_gu','address_dong',]
# class EditProfileForm(forms.ModelForm):``
#     class Meta:
#         model = User
#         fields = ('first_name', 'last_name', 'email', )

#     address = forms.CharField(max_length=255, required=True)
#     ph_num = forms.CharField(max_length=20, required=True)
#     nickname = forms.CharField(max_length=30, required=True)

#     def __init__(self, *args, **kwargs):
#         self.user = kwargs.pop('user')
#         super().__init__(*args, **kwargs)
#         profile = self.user.profile
#         self.fields['address'].widget.attrs.update({'value': profile.address})
#         self.fields['ph_num'].widget.attrs.update({'value': profile.ph_num})
#         self.fields['nickname'].widget.attrs.update({'value': profile.nickname})

#         for field_name in self.fields:
#             field = self.fields.get(field_name)
#             if field and isinstance(field, forms.CharField):
#                 field.widget.attrs.update({'class': 'form-control'})

#     def save(self, commit=True):
#         instance = super().save(commit=False)
#         profile = instance.profile
#         profile.address = self.cleaned_data['address']
#         profile.ph_num = self.cleaned_data['ph_num']
#         profile.nickname = self.cleaned_data['nickname']
#         if commit:
#             profile.save()
#         return instance