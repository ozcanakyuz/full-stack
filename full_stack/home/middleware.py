from django.http import HttpResponseForbidden
from .models import UserProfile
from full_stack import settings

# class SiteStatusMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         # Burada, duruma bağlı olarak sitemin kapatılma koşulunu kontrol edebilirsiniz.
#         # Örneğin, settings.py dosyanızda bir ayar (config) tanımlayabilirsiniz.

#         site_closed = getattr(settings, 'SITE_CLOSED', True)

#         if site_closed:
#             return HttpResponseForbidden("Site temporarily closed for maintenance.")

#         response = self.get_response(request)
#         return response

# PROFILE PHOTO
class UserProfileMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            profile = UserProfile.objects.get(user=request.user)
            request.user_profile = profile

        response = self.get_response(request)
        return response
