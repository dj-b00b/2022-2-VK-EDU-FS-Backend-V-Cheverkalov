from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST, require_GET

# Create your views here.

@require_GET
def show_user_page(request, user_id):
    user = {'id': user_id, 'nick': f'user{user_id}',
            'avatar': 'image.jpg', 'latest_activity': '14:30', 'phone_number': '8-800-555-35-35'}
    return JsonResponse({'user': user})
