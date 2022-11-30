from chats.serializers import ChatSerializer, ChatMemberSerializer
from chats.models import Chat, ChatMember
from users.models import User
from django.http import Http404
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, DestroyAPIView, UpdateAPIView


class ShowChatsCreateChat(ListCreateAPIView):
    serializer_class = ChatSerializer
    queryset = Chat.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        if 'users' not in request.data:
            return Response({'error': 'users - обязательное поле'}, status=400)
        
        if request.data['users'] == '':
            return Response({'error': 'в поле users ничего не передано!'}, status=400)
        
        if not isinstance(request.data['users'], list):
            return Response({'error': 'поле users не является типом list'}, status=400)
        lst_users_id = request.data['users']

        self.perform_create(serializer)

        chat = Chat.objects.all().last()
        creator = request.data['creator']
        category = request.data['category']

        if category == 2 and len(lst_users_id) > 2:
            return Response({'error': 'Вы не можете создать личный чат более чем на 2 участника'}, status=400)

        prepare_users = []
        for user_id in lst_users_id:
            user = get_object_or_404(User, id=user_id)
            prepare_users.append(
                ChatMember(
                    user_id=user.id,
                    chat_id=chat.id,
                     is_admin=True if creator == user.id and category == 1 else False
            ))
        ChatMember.objects.bulk_create(prepare_users)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
  

class ShowEditDeleteChat(RetrieveUpdateDestroyAPIView): 
    serializer_class = ChatSerializer
    queryset = Chat.objects.all() 

    
class ShowChatMembersAddChatMember(ListCreateAPIView):  
    serializer_class = ChatMemberSerializer   

    def get_queryset(self):
        chat = self.kwargs['pk']
        
        obj = get_list_or_404(ChatMember, chat_id=chat)
        return obj

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = request.data.get('user')
        chat_id = request.data.get('chat')
        if ChatMember.objects.filter(user_id=user, chat_id=chat_id).exists():
            return Response({'error': 'Указанный пользователь уже добавлен в чат!'}, status=400) 
        
        category = Chat.objects.get(id=chat_id).category.id
        count_users_chat = ChatMember.objects.filter(chat=chat_id)
        if category == 2 and len(count_users_chat) >= 2:
            return Response({'error': 'В личном чате не может состоять больше двух участников!'}, status=400) 

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class DelChatMember(DestroyAPIView):  
    serializer_class = ChatMemberSerializer
    queryset = ChatMember.objects.all()
    
    def get_object(self):
        user = self.kwargs['user_id']
        chat = self.kwargs['chat_id']

        obj = get_object_or_404(ChatMember, user_id=user, chat_id=chat)
        return obj
    

class AddRemoveAdmin(UpdateAPIView):  
    serializer_class = ChatMemberSerializer

    def get_object(self):
        user = self.kwargs['user_id']
        chat = self.kwargs['chat_id']

        obj = get_object_or_404(ChatMember, chat_id=chat, user_id=user)
        return obj

 
