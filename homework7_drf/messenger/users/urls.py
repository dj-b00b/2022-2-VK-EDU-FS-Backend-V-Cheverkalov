from django.urls import path
from users.views import *


urlpatterns = [
    path('api/v1.0/user/<int:pk>/', ShowInfoRemoveChangeDelUser.as_view()),
    path('api/v1.0/user/<int:user_id>/show_contacts/', ShowContactsAddContact.as_view()),
    path('api/v1.0/user/<int:user_id>/del_contact/<int:friend_id>/', DelContact.as_view(), name='del_user_from_contacts')
]
