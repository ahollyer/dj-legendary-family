from django import forms
from main.models import Post

class PostForm(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs = {
            'class': 'form-control input-lg',
            'placeholder': 'Write a post...'
        }
    ))

    class Meta:
        model = Post
        fields = ('post',)
