from django import forms
from .models import Movielog, Comment

class MovielogForm(forms.ModelForm):
    class Meta:
        model = Movielog
        fields =['title','director','release_day','body', 'image']
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author_name','comment_text')