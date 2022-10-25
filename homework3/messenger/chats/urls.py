from django.urls import path
from chats.views import chat_list, chat_create, chat_page

urlpatterns = [
    path('', chat_list, name='chat_list'),
    path('create/<int:num>', chat_create, name='create_chat'),
    path('page/<int:chat_id>', chat_page, name='chat_page')
]
