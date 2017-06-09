from accounts.models import UserProfile
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password'
        )

class UserInfoForm(forms.ModelForm):
    description = forms.CharField(required=False, widget=forms.Textarea(
        attrs = {
            'class': 'form-control',
            'placeholder': 'Enter a brief status, quote, bio, or whatever you want people to see about you!',
        }
    ))
    city = forms.CharField(required=False)
    website = forms.URLField(required=False)
    birthday = forms.DateField(required=False)
    image = forms.ImageField(required=False)

    class Meta:
        model = UserProfile
        exclude = ('user',)
