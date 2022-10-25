from django.urls import path
from users.views import show_user_page

urlpatterns = [
    path('<int:user_id>', show_user_page, name='user_page')
]
