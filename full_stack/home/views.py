from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render

from home.forms import LoginForm, SignUpForm
from home.models import Post, UserProfile

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
