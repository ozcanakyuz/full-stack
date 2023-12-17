from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from home.models import Comment, Post, PostForm, UserProfile
from user.forms import UserUpdateForm, ProfileUpdateForm

@login_required(login_url='/login') # Check login
def index(request):
        current_user = request.user
        profile = UserProfile.objects.get(user_id = current_user.pk)
        context = {'profile': profile,
                   'page': 'USER PROFILE',}
        return render(request, 'user_profile.html', context)

@login_required(login_url='/login') # Check login
def user_settings(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user) # request.user is user  data
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated!')
            return HttpResponseRedirect('/user')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)
        current_user = request.user
        profile = UserProfile.objects.get(user_id = current_user.pk)
        context = {'user_form': user_form,
                   'profile_form': profile_form,
                   'page':'SETTINGS',
                   'profile': profile,}
        return render(request, 'user_settings.html', context)

@login_required(login_url='/login')
def user_post(request):
    current_user = request.user
    posts = Post.objects.filter(user_id = current_user.id)
    profile = UserProfile.objects.get(user_id = current_user.pk)
    context = {'posts': posts,
               'profile': profile,
               'page': 'USER POSTS',}
    return render(request, 'user_posts.html', context)

@login_required(login_url='/login') # Check login
def user_deletepost(request,id):
    current_user = request.user
    Post.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request, 'Post deleted..')
    return HttpResponseRedirect('/user/post')

@login_required(login_url='/login')
def user_newpost(request):
    current_user = request.user
    profile = UserProfile.objects.get(user_id = current_user.pk)
    post = Post.objects.filter(user_id = current_user.id)
    context = {'page': 'USER NEW POST',
               'post': post,
               'profile': profile,}
    return render(request, 'user_newpost.html', context)
    
@login_required(login_url='/login')
def user_addpost(request):
    url = request.META.get('HTTP_REFERER')
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            data = Post() 
            data.title = form.cleaned_data['title']
            data.content = form.cleaned_data['content']
            data.image = form.cleaned_data['image']
            data.ip = request.META.get('REMOTE_ADDR')
            data.post_id = id
            current_user = request.user
            data.user_id = current_user.id
            data.save()
            messages.success(request, "Your post has been created.")
            return HttpResponseRedirect('/user/post')
        return HttpResponseRedirect(url)


@login_required(login_url='/login')
def user_comments(request):
    current_user = request.user
    profile = UserProfile.objects.get(user_id = current_user.pk)
    comments = Comment.objects.filter(user_id = current_user.id)
    context = {'comments': comments,
               'profile': profile,}
    return render(request, 'user_comments.html', context)

@login_required(login_url='/login') # Check login
def user_deletecomment(request,id):
    current_user = request.user
    Comment.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request, 'Comment deleted..')
    return HttpResponseRedirect('/user/comments')
        