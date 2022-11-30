from django.urls import path
from chats.views import *


urlpatterns = [
    path('api/v1.0/<int:pk>/', ShowChatsCreateChat.as_view()),
    path('api/v1.0/chat/<int:pk>/', ShowEditDeleteChat.as_view()),
    path('api/v1.0/chat/<int:pk>/members/', ShowChatMembersAddChatMember.as_view()),
    path('api/v1.0/chat/<int:chat_id>/del_member/<int:user_id>/', DelChatMember.as_view(), name='del_chat_member'), 
    path('api/v1.0/chat/<int:chat_id>/admin/<int:user_id>/', AddRemoveAdmin.as_view())
]
