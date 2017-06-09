from django import forms
from main.models import Post, Comment, Like

class PostForm(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(
        attrs = {
            'class': 'form-control input-lg',
            'placeholder': 'Start a new conversation...'
        }
    ))

    class Meta:
        model = Post
        fields = ('post',)

class CommentForm(forms.ModelForm):
    text = forms.CharField(widget=forms.TextInput(
        attrs = {
            'class': 'form-control input-lg',
            'placeholder': 'Write a comment...'
        }
    ))

    class Meta:
        model = Comment
        fields = ('text',)

class LikeForm(forms.ModelForm):
    like = forms.BooleanField(widget=forms.HiddenInput(), initial=True)

    class Meta:
        model = Like
        fields = ('like',)
