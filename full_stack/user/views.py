from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from home.models import Comment, Post, PostForm, ReplyComment, UserProfile, UserProfileForm
from user.forms import UserUpdateForm, ProfileUpdateForm

@login_required(login_url='/login') # Check login
def index(request):
    profile = UserProfile.objects.get_or_create(user=request.user)[0]
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        password_form = PasswordChangeForm(request.user, request.POST)
        if 'update_submit' in request.POST:
            if user_form.is_valid() and profile_form.is_valid():
                user_form.save()
                profile_form.save()
                messages.success(request, 'Your account has been updated!')
                return redirect('user_profile')
        elif 'password_submit' in request.POST:
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)  # Important!
                messages.success(request, 'Your password was successfully updated!')
                return HttpResponseRedirect('/user')
            else:
                messages.error(request, 'Please correct the error below.<br>'+ str(password_form.errors))
                return HttpResponseRedirect('/user')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)
        password_form = PasswordChangeForm(request.user)
        context = {'profile': profile,
                   'user_form': user_form,
                   'profile_form': profile_form,
                    'password_form': password_form,
                   'page': 'USER PROFILE',}
        return render(request, 'user_profile.html', context)

@login_required(login_url='/login') # Check login
def user_settings(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return HttpResponseRedirect('/user')
        else:
            messages.error(request, 'Please correct the error below.<br>'+ str(form.errors))
            return HttpResponseRedirect('/user/settings')
    else:
        form = PasswordChangeForm(request.user)
        current_user = request.user
        profile = UserProfile.objects.get(user_id = current_user.pk)
        context = {'form': form,
                   'profile': profile,
                   'page': 'USER SETTINGS'}
        return render(request, 'user_settings.html', context)

@login_required(login_url='/login') # Check login
def user_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  #! Important!
            messages.success(request, 'Your password was successfully updated!')
            return HttpResponseRedirect('/user')
        else:
            messages.error(request, 'Please correct the error below.<br>'+ str(form.errors))
            return HttpResponseRedirect('/user/password')
    else:
        form = PasswordChangeForm(request.user)
        return render(request, 'user_password.html', {'form': form})

@login_required(login_url='/login')
def user_post(request):
    current_user = request.user
    posts = Post.objects.filter(user_id = current_user.id)
    profile = UserProfile.objects.get(user_id=current_user.pk)
    paginator = Paginator(posts, 8)
    page_number = request.GET.get('page')
    
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    profile = UserProfile.objects.get(user_id = current_user.pk)
    context = {'posts': posts,
               'page_obj': page_obj,
               'profile': profile,
               'page': 'USER POSTS',}
    return render(request, 'user_posts.html', context)

@login_required(login_url='/login') # Check login
def user_deletepost(request,id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    Post.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request, 'Post deleted..')
    return HttpResponseRedirect(url)

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
            return HttpResponseRedirect(url)
        return HttpResponseRedirect(url)

@login_required(login_url='/login')
def user_comments(request):
    current_user = request.user
    profile = UserProfile.objects.get(user_id = current_user.pk)
    comments = Comment.objects.filter(user_id = current_user.id)
    repcomments = ReplyComment.objects.filter(user_id = current_user.id)
    context = {'comments': comments,
               'repcomments': repcomments,
               'profile': profile,
               'page': 'USER COMMENTS',}
    return render(request, 'user_comments.html', context)

@login_required(login_url='/login') # Check login
def user_deletecomment(request,id):
    current_user = request.user
    Comment.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request, 'Comment deleted..')
    return HttpResponseRedirect('/user/comments')

@login_required(login_url='/login') # Check login
def user_posts_update(request, id):
    post = get_object_or_404(Post, pk=id, user=request.user)
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('user_post')
    else:
        form = PostForm(instance=post)
    context = {'profile': profile,
               'form': form, 
               'post': post,
               'page': 'POST UPDATE',}
    return render(request, 'user_posts_update.html', context)