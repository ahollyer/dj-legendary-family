from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.urls import reverse
from django.views.generic import TemplateView, RedirectView
from main.forms import PostForm, CommentForm, LikeForm
from main.models import Post, Comment, Like

def home(request):
    return TemplateResponse(request, 'main/home.html', {})

def home_redirect(request):
    return redirect(reverse('main:home'))

@login_required
def about(request):
    return TemplateResponse(request, 'main/about.html', {})

@login_required
def photos(request):
    return TemplateResponse(request, 'main/photos.html', {})

@login_required
def get_comments(request, post_id):
    return TemplateResponse(request, 'main/comments.html', {'comments': comments})
    # To create api and render on front end:
    # return http.JsonResponse({'comments': comments})

@login_required
def rsvp(request):
    return TemplateResponse(request, 'main/rsvp.html', {})

class MainView(TemplateView):
    template_name = 'main/main.html'

    def get(self, request):
        form = PostForm()
        like = LikeForm()
        posts = Post.objects.order_by('-created')
        users = User.objects.all()
        context = {'postform': form, 'likeform': like, 'posts': posts, 'users': users}
        return TemplateResponse(request, self.template_name, context)

    def post(self, request):
        form_type = request.POST.get('form', '')
        like_form = LikeForm()
        post_form = PostForm()

        if form_type == 'like-form':
            like_form = LikeForm(request.POST)
            if like_form.is_valid():
                post = like_form.save(commit=False)
                post.user = request.user
                post.post_id = request.POST.get('post_id')
                post.save()
                return redirect('./')

        elif form_type == 'post-form':
            post_form = PostForm(request.POST)
            if post_form.is_valid():
                post = post_form.save(commit=False)
                post.user = request.user
                post.save()
                return redirect('./')

        context = {'likeform': like_form, 'postform': post_form}
        return TemplateResponse(request, self.template_name, context)


class PostView(TemplateView):
    template_name = 'main/post_detail.html'

    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        form = CommentForm()
        context = {'post': post, 'form': form}
        return TemplateResponse(request, self.template_name, context)

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = post
            comment.save()
            text = form.cleaned_data['text']
            return redirect('./')

        context = {'form': form, 'text': text}
        return TemplateResponse(request, self.template_name, context)
