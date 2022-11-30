from django.http import Http404
from messages.models import Message, UserReaction
from django.shortcuts import get_object_or_404, get_list_or_404
from messages.serializers import MessageSerializer, UserReactionSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView


class EditDeleteMessage(UpdateAPIView, DestroyAPIView):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()


class ShowMessagesCreateMessage(ListCreateAPIView):  
    serializer_class = MessageSerializer

    def get_queryset(self):
        chat = self.kwargs['pk']
        
        obj = get_list_or_404(Message, chat_id=chat)
        return obj


class AddReaction(CreateAPIView):  
    serializer_class = UserReactionSerializer
    queryset = UserReaction.objects.all()  

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = request.data.get('user')
        message = request.data.get('message') 

        if UserReaction.objects.filter(message_id=message, user_id=user).exists():
            return Response({'error': 'Вы уже поставили реакцию!'}, status=400)
        
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class UpdateDeleteReaction(UpdateAPIView, DestroyAPIView):   
   serializer_class = UserReactionSerializer

   def get_object(self):
        message = self.kwargs.get('message_id')  
        user = self.kwargs.get('user_id')

        obj = get_object_or_404(UserReaction, message_id=message, user_id=user)
        return obj

