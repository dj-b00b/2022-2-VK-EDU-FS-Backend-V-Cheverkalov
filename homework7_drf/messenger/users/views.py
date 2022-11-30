from django.http import Http404
from users.models import User, Contact
from django.shortcuts import get_object_or_404, get_list_or_404
from users.serializers import UserSerializer, ContactSerializer
from rest_framework.response import Response
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, DestroyAPIView
from rest_framework import status
from rest_framework.response import Response


class ShowInfoRemoveChangeDelUser(RetrieveUpdateDestroyAPIView):  
    serializer_class = UserSerializer
    queryset = User.objects.all()


class ShowContactsAddContact(ListCreateAPIView):
    serializer_class = ContactSerializer

    def get_queryset(self):
        user = self.kwargs['user_id']

        obj = get_list_or_404(Contact, user=user)
        return obj

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        phone_number = request.data.get('phone_number')
        if not User.objects.filter(phone_number=phone_number).exists():
            return Response(
                {'error': 'Данный номер телефона не зарегистрирован в мессенджере!'},
                status=400)
        
        friend = User.objects.filter(phone_number=request.data.get('phone_number'))
        if Contact.objects.filter(user_id=request.data.get('user'), friend=friend[0]).exists():
            return Response({'error': 'Такой пользователь уже добавлен в контакты!'})
        
        friend = User.objects.get(phone_number=request.data.get('phone_number')) 
        Contact.objects.create(
            user = User.objects.get(id=request.data.get('user')),
            name = request.data.get('name'),
            surname = request.data.get('surname'),
            phone_number = request.data.get('phone_number'),
            friend = friend
        )

        headers = self.get_success_headers(serializer.data)        
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class DelContact(DestroyAPIView):

   def get_object(self):
        friend = self.kwargs.get('friend_id')  
        user = self.kwargs.get('user_id')

        obj = get_object_or_404(Contact, friend_id=friend, user_id=user)
        return obj
