from django.urls import path
from messages.views import *


urlpatterns = [
    path('api/v1.0/<int:pk>/', ShowMessagesCreateMessage.as_view()),
    path('api/v1.0/message/<int:pk>/', EditDeleteMessage.as_view()),
    path('api/v1.0/message/add_reaction/', AddReaction.as_view(), name='add_reaction'),
    path('api/v1.0/message/<int:message_id>/edit_reaction/<int:user_id>/', UpdateDeleteReaction.as_view()),
]
