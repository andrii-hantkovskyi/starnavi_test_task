from django.urls import reverse
from rest_framework.views import APIView

from analytics.services.users import update_last_user_request


class LogUserRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            update_last_user_request(request.user.id)
            response = self.get_response(request)
            return response

        # Check if the request path is for Django admin
        if request.path.startswith(reverse('admin:index')):
            response = self.get_response(request)
            return response

        # Continue with your original logic for other URLs
        drf_request = APIView().initialize_request(request)
        user = drf_request.user

        if user.is_authenticated:
            update_last_user_request(user.id)

        response = self.get_response(request)
        return response