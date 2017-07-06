from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.urls import reverse
from django.views.generic import TemplateView, RedirectView
from main.forms import (PostForm, CommentForm, LikeForm, RsvpForm,
                        PhotoForm, PhotoTagForm, PhotoLikeForm)
from main.models import Post, Comment, Like, Rsvp, Photo

def home(request):
    return TemplateResponse(request, 'main/home.html', {})


def home_redirect(request):
    return redirect(reverse('main:home'))


@login_required
def about(request):
    return TemplateResponse(request, 'main/about.html', {})


@login_required
def get_comments(request, post_id):
    return TemplateResponse(request, 'main/comments.html', {'comments': comments})
    # To create api and render on front end:
    # return http.JsonResponse({'comments': comments})


class MainView(TemplateView):
    template_name = 'main/main.html'

    def get(self, request):
        form = PostForm()
        like = LikeForm()
        posts = Post.objects.order_by('-created')
        users = User.objects.all()
        context = {
            'postform': form,
            'likeform': like,
            'posts': posts,
            'users': users
        }
        return TemplateResponse(request, self.template_name, context)

    def post(self, request):
        form_type = request.POST.get('form', '')
        like_form = LikeForm()
        post_form = PostForm()

        if form_type == 'like-form':
            like_form = LikeForm(request.POST)
            if like_form.is_valid():
                like = like_form.save(commit=False)
                like.user = request.user
                like.post_id = request.POST.get('post_id')
                like.save()
                return redirect('./')

        elif form_type == 'post-form':
            post_form = PostForm(request.POST)
            if post_form.is_valid():
                post = post_form.save(commit=False)
                post.user = request.user
                post.save()
                return redirect('./')

        posts = Post.objects.order_by('-created')
        users = User.objects.all()
        context = {
            'likeform': like_form,
            'postform': post_form,
            'posts': posts,
            'users': users
        }
        return TemplateResponse(request, self.template_name, context)

class PhotoView(TemplateView):
    template_name = 'main/photos.html'

    def get(self, request):
        photo_form = PhotoForm()
        tag_form = PhotoTagForm()
        like_form = PhotoLikeForm()
        photos = Photo.objects.order_by('-uploaded')
        users = User.objects.all()
        context = {
            'photoform': photo_form,
            'tagform': tag_form,
            'likeform': like_form,
            'photos': photos,
            'users': users
        }
        return TemplateResponse(request, self.template_name, context)

    def post(self, request):
        form_type = request.POST.get('form', '')
        like_form = PhotoLikeForm()
        photo_form = PhotoForm()
        tag_form = PhotoTagForm()

        if form_type == 'like-form':
            like_form = PhotoLikeForm(request.POST)
            if like_form.is_valid():
                like = like_form.save(commit=False)
                like.user = request.user
                like.photo_id = request.POST.get('photo_id')
                like.save()
                return redirect('./')

        elif form_type == 'photo-form':
            photo_form = PhotoForm(request.POST, request.FILES)
            if photo_form.is_valid():
                photo = photo_form.save(commit=False)
                photo.user = request.user
                photo.save()
                return redirect('./')

        elif form_type == 'tag-form':
            tag_form = PhotoTagForm(request.POST)
            if tag_form.is_valid():
                tag = tag_form.save(commit=False)
                tag.user = request.user
                tag.save()
                return redirect('./')

        photos = Photo.objects.order_by('-uploaded')
        users = User.objects.all()
        context = {
            'likeform': like_form,
            'photoform': photo_form,
            'tagform': tag_form,
            'photos': photos,
            'users': users
        }
        return TemplateResponse(request, self.template_name, context)


class PhotoDetailView(TemplateView):
    template_name = 'main/photo_detail.html'

    def get(self, request, pk):
        photo = Photo.objects.get(pk=pk)
        form = CommentForm()
        context = {'photo': photo, 'form': form}
        return TemplateResponse(request, self.template_name, context)

    def post(self, request, pk):
        photo = Photo.objects.get(pk=pk)
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.photo = photo
            comment.save()
            text = form.cleaned_data['text']
            return redirect('./')

        context = {'form': form, 'text': text}
        return TemplateResponse(request, self.template_name, context)

@login_required
def edit_photo(request, photo_id):
    photo = get_object_or_404(Photo, pk=photo_id)
    if request.method == 'POST':
        photoform = PhotoForm(request.POST, instance=photo)
        if photoform.is_valid():
            photoform.save()
        return redirect(reverse('main:photos'))
    else:
        photoform = PhotoForm(instance=photo)
        context = {'photo': photo,'photoform': photoform}
        return TemplateResponse(request, 'main/edit_photo.html', context)


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


class RsvpView(TemplateView):
    template_name = 'main/rsvp.html'

    def get(self, request):
        form = RsvpForm()
        people = Rsvp.objects.all()
        context = {'form': form, 'people': people}
        return TemplateResponse(request, self.template_name, context)

    def post(self, request):
        form = RsvpForm(request.POST)

        if form.is_valid():
            submission = form.save()
            return redirect('./')
