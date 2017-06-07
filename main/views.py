from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.urls import reverse
from django.views.generic import TemplateView
from main.forms import PostForm

def home(request):
    return TemplateResponse(request, 'main/home.html', {})

def home_redirect(request):
    return redirect(reverse('main:home'))

class MainView(TemplateView):
    template_name = 'main/main.html'

    def get(self, request):
        form = PostForm()
        context = {'form': form}
        return TemplateResponse(request, self.template_name, context)

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['post']
            return redirect('main:main')
        context = {'form': form, 'text': text}
        return TemplateResponse(request, self.template_name, context)
