from django.core import validators
from django import forms
from .models import Article

class PostArticle(forms.ModelForm):
     class Meta:
         model=Article
         fields=['title','text']
         labels={'title':'Title','text':'Descripton'}
