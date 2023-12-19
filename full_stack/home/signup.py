    # if request.method == 'POST':
    #     login_form = LoginForm(request.POST)
    #     # signup_form = SignUpForm(request.POST)
    #     if 'login_submit' in request.POST:
    #         if login_form.is_valid():
    #             username = login_form.cleaned_data['username']
    #             password = login_form.cleaned_data['password']
    #             user = authenticate(username=username, password=password)
    #             if user is not None:
    #                 login(request, user)
    #                 messages.success(request, "You have successfully logged in {}".format(user.username))
    #                 return HttpResponseRedirect('/')
    #             else:
    #                 messages.warning(request, "Girilen Bilgiler Hatali Tekrar Deneyiniz {}".format(username))
    #                 return HttpResponseRedirect('/')
    #     # elif request.method == "POST":
    #     #     if signup_form.is_valid():
    #     #         signup_form.save()
    #     #         username = signup_form.cleaned_data.get('username')
    #     #         password = signup_form.cleaned_data.get('password1')
    #     #         user = authenticate(username=username, password=password)
    #     #         login(request, user)
    #     #         current_user = request.user
    #     #         data=UserProfile()
    #     #         data.user_id=current_user.id
    #     #         data.image="images/users/user.png"
    #     #         data.save()
    #     #         messages.success(request, 'Your account has been created!')
    #     #         return HttpResponseRedirect('/')
    #     #     else:
    #     #         messages.warning(request, login_form.errors)
    #     #         return HttpResponseRedirect('/')
    #     # else:
    #     #     login_form = LoginForm
    #         # signup_form = signup_form()
    # if request.user.is_authenticated:
    #     current_user = request.user
    #     profile = UserProfile.objects.get(user_id=current_user.pk)
    #     posts = Post.objects.filter(status='True')
    #     login_form = LoginForm
    #     # signup_form = signup_form()
    #     context = {'login_form': login_form,
    #             #    'signup_form': signup_form,
    #                'profile': profile,
    #                'posts': posts,
    #                'page': 'Home',} 
    #     return render(request, 'index.html', context)
    # else:
    #     login_form = LoginForm
    #     posts = Post.objects.filter(status='True')
    #     context = {'login_form': login_form,
    #                'posts': posts,
    #                'page': 'Home',} 
    #     return render(request, 'index.html', context)
