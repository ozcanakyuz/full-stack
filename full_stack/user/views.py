from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from home.models import Post, PostForm, UserProfile

def index(request):
    current_user = request.user
    profile = UserProfile.objects.get(user_id = current_user.pk)
    context = {'profile': profile,
               'page': 'USER PROFILE',}
    return render(request, 'user_profile.html', context)

def user_settings(request):
    current_user = request.user
    profile = UserProfile.objects.get(user_id = current_user.pk)
    context = {'profile': profile,
               'page': 'USER SETTINGS',}
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