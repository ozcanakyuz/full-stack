from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.shortcuts import render

from home.forms import LoginForm
from home.models import UserProfile

#! LOG IN
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

    form = LoginForm
    context = {'form': form,
               'page': 'Home',} 
    return render(request, 'index.html', context)

@login_required(login_url='/login') # Check login
def navbar(request):
    current_user = request.user
    profile = UserProfile.objects.get(user_id = current_user.pk)
    context = {'profile': profile}
    return render(request, 'navbar.html', context)

# def login_view(request):
#     if request.method == 'POST':  #check post
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(username=username, password=password)

#             if user is not None:
#                 login(request, user)
#                 messages.success(request, "You have successfully logged in {}".format(user.username))
#                 return HttpResponseRedirect('/home')
#             else:
#                 messages.warning(request, "Girilen Bilgiler Hatali Tekrar Deneyiniz {}".format(username))
#                 return HttpResponseRedirect('/')

#     form = LoginForm
#     context = {'form': form,} 
#     return render(request, 'index.html', context)

#! LOG OUT
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

#! SIGN-UP
