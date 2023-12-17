from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render


from home.forms import CommentForm, LoginForm, SignUpForm
from home.models import Comment, Post, ReplyComment, ReplyCommentForm, UserProfile

#! LOG IN & SIGN-UP
def index(request):
    if request.method == 'POST':  #check post
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have successfully logged in {}".format(user.username))
                return HttpResponseRedirect('/')
            else:
                messages.warning(request, "Girilen Bilgiler Hatali Tekrar Deneyiniz {}".format(username))
                return HttpResponseRedirect('/')
    # elif request.method == "POST":
    #     form = SignUpForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         username = form.cleaned_data.get('username')
    #         password = form.cleaned_data.get('password')
    #         user = authenticate(username=username, password=password)
    #         login(request, user)
    #         #?Create data in profile table for user
    #         current_user = request.user
    #         data = UserProfile()
    #         data.user_id = current_user.id
    #         data.image="images/users/user.png"
    #         data.save()
    #         messages.success(request, 'Your account has been created!')
    #         return HttpResponseRedirect('/')
        else:
            messages.warning(request, form.errors)
            return HttpResponseRedirect('/')
    posts = Post.objects.filter(status=True)
    formlog = LoginForm
    # formsign = SignUpForm
    context = {'formlog': formlog,
               # 'formsign': formsign,
               'posts': posts,
               'page': 'Home',} 
    return render(request, 'index.html', context)


#! LOG OUT
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

def post_detail(request, id):
    if request.user.is_authenticated:
        #* Kullanıcı giriş yapmışsa, istediğiniz postları çek
        current_user = request.user
        profile = UserProfile.objects.get(user_id = current_user.pk)
        comments = Comment.objects.filter(post_id=id, status=True)
        repcomments = ReplyComment.objects.all() # comment_id=id, status=True
        post_detail = Post.objects.get(pk=id)
        context = {'post_detail': post_detail,
                    'comments': comments,
                    'repcomments': repcomments,
                    'profile': profile,}
        return render(request, 'post_detail.html', context)
    else:
        comments = Comment.objects.filter(post_id=id, status=True)
        repcomments = ReplyComment.objects.filter(comment_id=id) #, status=True
        post_detail = Post.objects.get(pk=id)
        context = {'post_detail': post_detail,
                   'comments': comments,
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
            messages.warning(request, "Lütfen mesaj kutucuklarini doldurunuz!!") 
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
            messages.warning(request, "Lütfen mesaj kutucuklarini doldurunuz!!") 
    return HttpResponseRedirect(url)