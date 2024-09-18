from django.utils.deprecation import MiddlewareMixin
from django.utils import timezone

from chat.models import UserActivity


class UserActivityMiddleware(MiddlewareMixin):

    # def __init__(self, get_response):
    #     self.get_response = get_response
    

    def process_request(self, request):
        if request.user.is_authenticated:
            UserActivity.objects.update_or_create(user=request.user, defaults={'last_activity': timezone.now()})
