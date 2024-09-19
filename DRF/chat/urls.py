from django.urls import path

from chat import views


app_name = "chat"

urlpatterns = [
    path("start/conversation/", views.ConversationAPIView.as_view(), name='start-conversation'),

    path("get/conversation/<int:convo_id>/", views.ConversationAPIView.as_view(), name='conversation'),

    path("all/conversations/", views.AllConversionsAPIView.as_view(), name='conversations'),
]
