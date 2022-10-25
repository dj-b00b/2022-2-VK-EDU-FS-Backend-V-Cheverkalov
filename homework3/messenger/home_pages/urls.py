from django.urls import path
from home_pages.views import render_home_page

urlpatterns = [
    path('', render_home_page, name='home_page')
]
