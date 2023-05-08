from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, PasswordChangeForm
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'profile_img',
            'email',
            'last_name',
            'first_name',
            'password1',
            'password2',
            'birthday'
        )
        label_suffix = ''
    
    username = forms.CharField(label='ID', label_suffix='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'style': 'width: 374.4px;'}))
    profile_img = forms.ImageField(label='프로필 사진', label_suffix='', required=False, widget=forms.ClearableFileInput(
        attrs={'class': 'form-control', 'style': 'width: 374.4px;'}))
    email = forms.EmailField(label='이메일', label_suffix='', widget=forms.EmailInput(
        attrs={'class': 'form-control', 'style': 'width: 374.4px;'}))
    last_name = forms.CharField(label='성', label_suffix='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'style': 'width: 374.4px;'}))
    first_name = forms.CharField(label='이름', label_suffix='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'style': 'width: 374.4px;'}))

    password1 = forms.CharField(label='비밀번호', label_suffix='', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'style': 'width: 374.4px;'}))
    password2 = forms.CharField(label='비밀번호 확인', label_suffix='', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'style': 'width: 374.4px;'}))
    birthday = forms.DateField(label='생년월일', label_suffix='', widget=forms.DateInput(
        attrs={'class': 'form-control', 'type': 'date',  'style': 'width: 374.4px;'}))


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('profile_img','email', 'last_name', 'first_name',  'birthday')
        label_suffix = ''

    profile_img = forms.ImageField(label='프로필 사진', label_suffix='', required=False, widget=forms.ClearableFileInput(
        attrs={'class': 'form-control', 'style': 'width: 374.4px;'}))
    email = forms.EmailField(label='이메일', label_suffix='', widget=forms.EmailInput(
        attrs={'class': 'form-control', 'style': 'width: 374.4px;'}))
    last_name = forms.CharField(label='성', label_suffix='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'style': 'width: 374.4px;'}))
    first_name = forms.CharField(label='이름', label_suffix='', widget=forms.TextInput(
        attrs={'class': 'form-control', 'style': 'width: 374.4px;'}))
    birthday = forms.DateField(label='생년월일', label_suffix='', widget=forms.DateInput(
        attrs={'class': 'form-control', 'type': 'date',  'style': 'width: 374.4px;'}))
    password = None


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="아이디",
        label_suffix='',
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'style': 'width: 374.4px;'})
    )

    password = forms.CharField(
        label="비밀번호",
        label_suffix='',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'style': 'width: 374.4px;'})
    )


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="기존 비밀번호",
        label_suffix='',
        required=True,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'style': 'width: 374.4px;'})
    )

    new_password1 = forms.CharField(
        label="새로운 비밀번호",
        label_suffix='',
        required=True,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'style': 'width: 374.4px;'})
    )

    new_password2 = forms.CharField(
        label="새로운 비밀번호 확인",
        label_suffix='',
        required=True,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'style': 'width: 374.4px;'})
    )

