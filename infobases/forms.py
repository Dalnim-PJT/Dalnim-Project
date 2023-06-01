from django import forms
from .models import Info, Comment, Image

class InfoForm(forms.ModelForm):
    title = forms.CharField(
        label='',
        label_suffix='',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'create--form-control',
                'style': 'width: 100%;',
            }
        )
    )
    content = forms.CharField(
        label='',
        label_suffix='',
        required=True,
        widget=forms.Textarea(
            attrs={
                'class': 'create--form-control',
                'style': 'width: 100%;',
            }
        )
    )
    class Meta:
        model = Info
        fields = ('title', 'content',)

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image',)
        widgets = {'image': forms.ClearableFileInput(attrs={'multiple': True, 'class': 'form-control'})}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
    content = forms.CharField(
        label = '',
        label_suffix='',
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control', 

            })
    )
