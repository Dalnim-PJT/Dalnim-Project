from django import forms
from .models import Info, Comment, Image

class InfoForm(forms.ModelForm):
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
    
