from django.urls import path
from messages.views import *

urlpatterns = [
    path('create/', create_message, name='create_message'),
    path('edit/', edit_message, name='edit_message'),
    path('read/', read_message, name='read_message'),
    path('del/', del_message, name='del_message'),
    path('show/', show_list_messages, name='show_messages'),
    path('add_reaction/', add_reaction, name='add_reactions'),
    path('del_reaction/', del_reaction, name='del_reactions'),
]
