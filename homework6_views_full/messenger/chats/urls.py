from django.urls import path
from chats.views import *

urlpatterns = [
    path('', show_chat_list, name='show_chat_list'),
    path('create/', create_chat, name='create_chat'),
    path('edit/', edit_chat, name='edit_chat'),
    path('add_member/', add_chat_member, name='add_chat_member'),
    path('del_member/', del_chat_member, name='del_chat_member'),
    path('del/', del_chat, name='del_chat'),
    path('info/', show_chat_info, name='show_chat_info'),
    path('add_admin/', add_chat_admin, name='add_admin_chat'),
    path('del_admin/', del_chat_admin, name='del_admin_chat'),
]
