from django.urls import path
from users.views import *


urlpatterns = [
    path('', get_info_about_user, name='user_info'),
    path('change/', change_info_about_user, name='change_user_info'),
    path('show_contacts/', show_list_contacts, name='show_user_contacts'),
    path('add_contact/', add_user_to_contacts, name='add_user_to_contacts'),
    path('del_contact/', del_user_from_contacts, name='del_user_from_contacts')
]
