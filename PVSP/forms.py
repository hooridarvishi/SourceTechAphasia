#
# from django import forms
# from .models import Post
#
# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = ['text', 'image']

from django import forms
from .models import *

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['content']

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image']