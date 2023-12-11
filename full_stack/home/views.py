from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render

from home.forms import LoginForm

def index(request):
    return render(request, 'index.html', {'page': 'Home'})


#! LOG IN 
def login_view(request):
    if request.method == 'POST':  # check post
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                #? messages.success(request, "Başarılı şekilde oturum açtınız {}".format(user.username))
                return HttpResponseRedirect('/home')
            else:
                messages.warning(request, "Girilen Bilgiler Hatalı Tekrar Deneyiniz {}".format(username))
                return HttpResponseRedirect('/login')

    form = LoginForm
    context = {'form': form}
    return render(request, 'login.html', context)
