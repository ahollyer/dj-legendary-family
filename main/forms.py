from django import forms
from django.contrib.auth.models import User
from main.models import (Post, Comment, Like, Rsvp,
                        Photo, PhotoLike)

################### POSTS/COMMENTS ################
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

################### RSVPs ###################
class RsvpForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs = {
            'class': 'form-control input-lg',
            'placeholder': 'Name'
        }
    ))
    rsvp = forms.BooleanField(initial=True, required=False)
    bringing = forms.CharField(widget=forms.TextInput(
        attrs = {
            'class': 'form-control input-lg',
            'placeholder': 'Bringing anything cool? (food, games, etc.)'
        }
    ), required=False)

    class Meta:
        model = Rsvp
        fields = ('name', 'rsvp', 'bringing')


#################### FAMILY PHOTOS ########################

class PhotoForm(forms.ModelForm):
    image = forms.ImageField(required=False)
    date_taken = forms.DateField(required=False)
    location = forms.CharField(required=False,
    widget=forms.TextInput(
        attrs = {
            'class': 'form-inline',
        }
    ))
    description = forms.CharField(required=False, widget=forms.Textarea(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Enter a brief description to be displayed with your photo.',
        }
    ))

    class Meta:
        model = Photo
        widgets = {
            'tagz': forms.CheckboxSelectMultiple(),
        }
        fields = ('image', 'date_taken', 'location', 'description', 'tagz')

    def __init__(self, *args, **kwargs):
        super(PhotoForm, self).__init__(*args, **kwargs)
        self.fields['tagz'].queryset = User.objects.order_by('username')

class PhotoLikeForm(forms.ModelForm):
    like = forms.BooleanField(widget=forms.HiddenInput(), initial=True)

    class Meta:
        model = PhotoLike
        fields = ('like',)
