from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from home.models import UserProfile

def index(request):
    current_user = request.user
    profile = UserProfile.objects.get(user_id = current_user.pk)
    context = {'profile': profile,
               'page': 'USER PROFILE',}
    return render(request, 'user_profile.html', context)