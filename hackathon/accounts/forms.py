from django import forms
from django.contrib.auth.forms import UserChangeForm

from .models import Profile, User


class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', )

    address = forms.CharField(max_length=255, required=True)
    ph_num = forms.CharField(max_length=20, required=True)
    nickname = forms.CharField(max_length=30, required=True)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        profile = self.user.profile
        self.fields['address'].widget.attrs.update({'value': profile.address})
        self.fields['ph_num'].widget.attrs.update({'value': profile.ph_num})
        self.fields['nickname'].widget.attrs.update({'value': profile.nickname})

        for field_name in self.fields:
            field = self.fields.get(field_name)
            if field and isinstance(field, forms.CharField):
                field.widget.attrs.update({'class': 'form-control'})
