from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST, require_GET

# Create your views here.
chats = []


@require_GET
def chat_list(request):
    return JsonResponse({'chats': chats})


@require_POST
def chat_create(request, num):
    check_exist_chat = list(map(lambda x: x['id'] != num, chats))
    if False not in check_exist_chat:
        chats.append({
            'id': num, 
            'title': f'chat {num}',
            'messagesq': 0, 
            'users': ['vova', 'katya']
        })
    return JsonResponse({'create_chat': chats})


@require_GET
def chat_page(request, chat_id):
    requested_chat = [i for i in range(len(chats)) if chats[i]['id'] == chat_id]
    if not requested_chat:
        return HttpResponseNotFound()
    return JsonResponse({'chat': chats[requested_chat[0]]}) 
