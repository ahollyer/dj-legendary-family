from accounts.forms import RegistrationForm, EditProfileForm, UserInfoForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.urls import reverse

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:view_profile'))
    else:
        form = RegistrationForm()
        context = {'form': form}
        return TemplateResponse(request, 'accounts/reg_form.html', context)

@login_required
def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    context = {'user': user}
    return TemplateResponse(request, 'accounts/profile.html', context)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        userform = EditProfileForm(request.POST, instance=request.user)
        infoform = UserInfoForm(request.POST, request.FILES, instance=request.user.userprofile)
        if userform.is_valid():
            userform.save()
        if infoform.is_valid():
            infoform.user = request.user
            infoform.save()
        return redirect(reverse('accounts:view_profile'))
    else:
        userform = EditProfileForm(instance=request.user)
        infoform = UserInfoForm(instance=request.user.userprofile)
        context = {'userform': userform, 'infoform': infoform}
        return TemplateResponse(request, 'accounts/edit_profile.html', context)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('accounts:view_profile'))
        else:
            return redirect(reverse('accounts:change_password'))
    else:
        form = PasswordChangeForm(user=request.user)
        context = {'form': form,}
        return TemplateResponse(request, 'accounts/change_password.html',
            context)
