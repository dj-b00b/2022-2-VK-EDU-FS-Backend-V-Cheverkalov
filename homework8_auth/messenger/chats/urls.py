from django.urls import path
from chats.views import *


urlpatterns = [
    path('api/v1.0/<int:pk>/', my_login_required(ShowChatsCreateChat.as_view())),
    path('api/v1.0/chat/<int:pk>/',my_login_required(ShowEditDeleteChat.as_view())),
    path('api/v1.0/chat/<int:pk>/members/', my_login_required(ShowChatMembersAddChatMember.as_view())),
    path('api/v1.0/chat/<int:chat_id>/del_member/<int:user_id>/', my_login_required(DelChatMember.as_view()), name='del_chat_member'), 
    path('api/v1.0/chat/<int:chat_id>/admin/<int:user_id>/', my_login_required(AddRemoveAdmin.as_view()))
]
