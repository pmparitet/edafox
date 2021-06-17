from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, UserCreationForm
from .models import FoxUser


class FoxUserLoginForm(AuthenticationForm):
    class Meta:
        model = FoxUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(FoxUserLoginForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class FoxUserRegisterForm(UserCreationForm):
    class Meta:
        model = FoxUser
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 'email', 'phone_number', 'birthday', 'gender', 'avatar')

    def __init__(self, *args, **kwargs):
        super(FoxUserRegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class FoxUserEditForm(UserChangeForm):
    class Meta:
        model = FoxUser
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'birthday', 'gender', 'avatar')

    def __init__(self, *args, **kwargs):
        super(FoxUserEditForm, self).__init__(*args, **kwargs)
        self.fields['username'].disabled = True
        self.fields['email'].disabled = True
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()
