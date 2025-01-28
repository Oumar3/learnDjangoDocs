from django import forms

from app.models import blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = blog
        fields = ['name','img']