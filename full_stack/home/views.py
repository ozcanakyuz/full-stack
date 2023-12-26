from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from home.forms import CommentForm, LoginForm, SearchForm, SignUpForm
from home.models import Comment, Post, ReplyComment, ReplyCommentForm, UserProfile

#! LOG IN & SIGN-UP
def index(request):
    if request.method == 'POST':  #check post
        login_form = LoginForm(request.POST)
        signup_form = SignUpForm(request.POST)
        if 'login_submit' in request.POST:     #! LOG IN FORM
            if login_form.is_valid():
                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, "You have successfully logged in {}".format(user.username))
                    return HttpResponseRedirect('/')
                else:
                    messages.warning(request, "The Information Entered Is Incorrect, Try Again! {}".format(username))
                    return HttpResponseRedirect('/')
        elif 'signup_submit' in request.POST:  #! SIGN UP FORM
            if signup_form.is_valid():
                signup_form.save()
                username = signup_form.cleaned_data.get('username')
                password = signup_form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                login(request, user)
                current_user = request.user
                data = UserProfile()
                data.user_id = current_user.id
                data.image="images/users/user.png"
                data.save()
                messages.success(request, 'Your account has been created!')
                return HttpResponseRedirect('/user')
            else:
                messages.warning(request, signup_form.errors)
                return HttpResponseRedirect('/')
        else:
            login_form = LoginForm()
            signup_form = SignUpForm()
    if request.user.is_authenticated:
        posts = Post.objects.filter(status=True)
        paginator = Paginator(posts, 8)
        page_number = request.GET.get('page')
        
        try:
            page_obj = paginator.get_page(page_number)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)

        current_user = request.user
        profile = UserProfile.objects.get(user_id=current_user.pk)
        posts = Post.objects.filter(status='True')
        login_form = LoginForm()
        signup_form = SignUpForm()
        context = {'login_form': login_form,
                   'signup_form': signup_form,
                    'profile': profile,
                    'page_obj': page_obj,
                    'page': 'Home',} 
        return render(request, 'index.html', context)
    else:
        posts = Post.objects.filter(status=True)
        paginator = Paginator(posts, 8)
        page_number = request.GET.get('page')
        
        try:
            page_obj = paginator.get_page(page_number)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)

        login_form = LoginForm()
        signup_form = SignUpForm()
        context = {'login_form': login_form,
                   'signup_form': signup_form,
                   'page_obj': page_obj,
                   'page': 'Home',} 
        return render(request, 'index.html', context)

#! LOG OUT
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def post_detail(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':  #check post
        login_form = LoginForm(request.POST)
        signup_form = SignUpForm(request.POST)
        if 'login_submit' in request.POST:     #! LOG IN FORM
            if login_form.is_valid():
                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, "You have successfully logged in {}".format(user.username))
                    return HttpResponseRedirect('/')
                else:
                    messages.warning(request, "The Information Entered Is Incorrect, Try Again! {}".format(username))
                    return HttpResponseRedirect('/')
        elif 'signup_submit' in request.POST:  #! SIGN UP FORM
            if signup_form.is_valid():
                signup_form.save()
                username = signup_form.cleaned_data.get('username')
                password = signup_form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                login(request, user)
                current_user = request.user
                data = UserProfile()
                data.user_id = current_user.id
                data.image="images/users/user.png"
                data.save()
                messages.success(request, 'Your account has been created!')
                return HttpResponseRedirect('/user')
            else:
                messages.warning(request, signup_form.errors)
                return HttpResponseRedirect('/')
        else:
            login_form = LoginForm()
            signup_form = SignUpForm()
    if request.user.is_authenticated:
        current_user = request.user
        profile = UserProfile.objects.get(user_id = current_user.pk)
        comments = Comment.objects.filter(post_id=id, status='True')
        repcomments = ReplyComment.objects.filter(comment_id=id, status='True') #? "status=True" not working!
        post_detail = Post.objects.get(pk=id)
        context = {'post_detail': post_detail,
                    'comments': comments,
                    'repcomments': repcomments,
                    'profile': profile,}
        return render(request, 'post_detail.html', context)
    else:
        comments = Comment.objects.filter(post_id=id, status='True')
        repcomments = ReplyComment.objects.filter(comment_id=id, status='True')
        post_detail = Post.objects.get(pk=id)
        posts = Post.objects.filter(status='True')
        formlog = LoginForm
        context = {'post_detail': post_detail,
                   'comments': comments,
                   'formlog': formlog,
                    'posts': posts,
                   'repcomments': repcomments,
                   'page': 'POST DETAIL',}
        return render(request, 'post_detail.html', context)

def addcomment(request,id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = Comment() 
            data.comment = form.cleaned_data['comment']
            data.ip = request.META.get('REMOTE_ADDR')
            data.post_id=id
            current_user= request.user
            data.user_id=current_user.id
            data.save() 
            messages.success(request, "Your review has been sent. Thank you for your interest.")
            return HttpResponseRedirect(url)
        else:
            messages.warning(request, "Please do not leave the message boxes empty!") 
    return HttpResponseRedirect(url)

def replycomment(request, id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = ReplyCommentForm(request.POST)
        if form.is_valid():
            data = ReplyComment() 
            data.repcomment = form.cleaned_data['repcomment']
            data.ip = request.META.get('REMOTE_ADDR')
            data.comment_id=id
            current_user= request.user
            data.user_id=current_user.id
            data.save()
            messages.success(request, 'Comment replied!')
            return HttpResponseRedirect(url)
        else:
            messages.warning(request, "Please do not leave the message boxes empty!") 
    return HttpResponseRedirect(url)

def search(request):
    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        login_form = LoginForm(request.POST)
        signup_form = SignUpForm(request.POST)
        if 'login_submit' in request.POST:
            if login_form.is_valid():
                username = login_form.cleaned_data['username']
                password = login_form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, "You have successfully logged in {}".format(user.username))
                    return HttpResponseRedirect('/')
                else:
                    messages.warning(request, "Information entered is wrong. Please try again {}".format(username))
                    return HttpResponseRedirect('/')
        elif 'signup_submit' in request.POST:
            if signup_form.is_valid():
                signup_form.save()
                username = signup_form.cleaned_data.get('username')
                password = signup_form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                login(request, user)
                current_user = request.user
                data = UserProfile()
                data.user_id = current_user.id
                data.image="images/users/user.png"
                data.save()
                messages.success(request, 'Your account has been created!')
                return HttpResponseRedirect('/user')
            else:
                messages.warning(request, signup_form.errors)
                return HttpResponseRedirect('/')
        elif search_form.is_valid():
            if request.user.is_authenticated:
                current_user = request.user
                profile = UserProfile.objects.get(user_id=current_user.pk)
                query = search_form.cleaned_data['query']
                posts = Post.objects.filter(content__icontains=query)
                context = {'posts': posts,
                        'query': query,
                        'profile': profile,
                        'page': 'SEARCH',}
                return render(request, 'search.html', context)
            else:
                query = search_form.cleaned_data['query']
                posts = Post.objects.filter(content__icontains=query)
                context = {'posts': posts,
                        'query': query,
                        'page': 'SEARCH',}
                return render(request, 'search.html', context)
    else:
        login_form = LoginForm()
        signup_form = SignUpForm()
    if request.user.is_authenticated:
        current_user = request.user
        profile = UserProfile.objects.get(user_id=current_user.pk)
        posts = Post.objects.filter(status='True')
        login_form = LoginForm
        signup_form = SignUpForm
        context = {'login_form': login_form,
                   'signup_form': signup_form,
                    'profile': profile,
                    'posts': posts,
                    'page': 'Home',} 
        return render(request, 'index.html', context)
    else:
        posts = Post.objects.filter(status='True')
        login_form = LoginForm
        signup_form = SignUpForm
        context = {'login_form': login_form,
                   'signup_form': signup_form,
                    'posts': posts,
                    'page': 'Home',} 
        return render(request, 'index.html', context)