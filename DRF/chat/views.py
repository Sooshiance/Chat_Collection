from django.shortcuts import render
from django.shortcuts import redirect, reverse
from django.db.models import Q

from rest_framework import generics, response, status, permissions

from .models import Conversation
from .serializers import ConversationListSerializer, ConversationSerializer
from user.models import User


class StartConversation(generics.GenericAPIView):
    """"""

    serializer_class = ConversationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = request.data
        username = data.pop('username')
        try:
            participant = User.objects.get(username=username)
        except User.DoesNotExist:
            return response.Response({'message': 'You cannot chat with a non existent user'})

        conversation = Conversation.objects.filter(Q(initiator=request.user, receiver=participant) |
                                                Q(initiator=participant, receiver=request.user))
        if conversation.exists():
            return redirect(reverse('get_conversation', args=(conversation[0].id,)))
        else:
            conversation = Conversation.objects.create(initiator=request.user, receiver=participant)
            return response.Response(ConversationSerializer(instance=conversation).data)


class ConversationAPIView(generics.GenericAPIView):
    """
    
    """
    serializer_class = ConversationSerializer

    def get(self, request, convo_id, *args, **kwargs):
        conversation = Conversation.objects.filter(id=convo_id)
        if not conversation.exists():
            return response.Response({'message': 'Conversation does not exist'})
        else:
            serializer = ConversationSerializer(instance=conversation[0])
            return response.Response(serializer.data)


class AllConversionsAPIView(generics.GenericAPIView):
    """
    
    """

    serializer_class = ConversationListSerializer

    def get(self, request, *args, **kwargs):
        conversation_list = Conversation.objects.filter(Q(initiator=request.user) |
                                                    Q(receiver=request.user))
        serializer = ConversationListSerializer(instance=conversation_list, many=True)
        return response.Response(serializer.data)
