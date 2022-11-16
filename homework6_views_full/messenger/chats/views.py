from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from chats.models import Chat, Category, ChatMember
from users.models import User
from django.shortcuts import get_object_or_404
import json
# Create your views here.


def serialize_users_json(obj):
    chat_members = ChatMember.objects.filter(chat_id=obj.id)
    users_list = []

    for chat_member in chat_members:
        user = User.objects.get(id=chat_member.user_id)
        users_list.append({
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'about_user': user.about_user,
            'phone_number': user.phone_number,
            'avatar': str(user.avatar),
        })
    return users_list


def serialize_admins_json(obj):
    admins = ChatMember.objects.filter(chat_id=obj.id, is_admin=True)
    admins_list = []

    for admin in admins:
        print(admin)
        user = User.objects.get(id=admin.user_id)
        admins_list.append({
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'about_user': user.about_user,
            'phone_number': user.phone_number,
            'avatar': str(user.avatar),
        })
    return admins_list


@require_http_methods(['POST'])
def create_chat(request):
    required_params = ['title', 'creator', 'category', 'users']
    for param in required_params:
        if param not in request.POST.keys():
            return JsonResponse({'error': f'A required parametr {param.upper()} was not passed'}, status=400)

    creator = get_object_or_404(User, id=request.POST['creator'])
    category = get_object_or_404(Category, id=request.POST['category'])

    chat = Chat.objects.create(
        title=request.POST['title'],
        description=request.POST.get('description', ''),
        creator=creator,
        category=category
    )

    for user_id in request.POST['users'].split(','):
        user = get_object_or_404(User, id=user_id)

        ChatMember.objects.create(
            user_id=user.id,
            chat_id=chat.id,
            is_admin=True if creator.id == user.id and category.id == 1 else False
        )

    return JsonResponse({
        'chat': {
            'title': chat.title,
            'description': chat.description,
            'creator': str(chat.creator),
            'category': str(chat.category),
            'users': serialize_users_json(chat),
            'admins': serialize_admins_json(chat)
        }
    })


@require_http_methods(['PUT'])
def edit_chat(request):
    body = json.loads(request.body)
    chat = get_object_or_404(Chat, id=body.get('id'))

    for field, value in body.items():
        setattr(chat, field, value)
        chat.save()

    return JsonResponse({
        'chat': {
            'title': chat.title,
            'description': chat.description,
            'creator': str(chat.creator),
            'category': str(chat.category),
            'users': serialize_users_json(chat),
            'admins': serialize_admins_json(chat)
        }
    })


@require_http_methods(['GET'])
def show_chat_list(request):
    chats = Chat.objects.all()
    chat_list = []
    for chat in chats:
        chat_list.append({
            'title': str(chat.title),
            'description': str(chat.description),
            'creator': str(chat.creator),
            'category': str(chat.category),
        })
    return JsonResponse({'chats': chat_list})


@require_http_methods(['POST'])
def add_chat_member(request):
    chat = get_object_or_404(Chat, id=request.POST['chat_id'])
    user = get_object_or_404(User, id=request.POST['user_id'])

    if not ChatMember.objects.filter(user_id=user.id, chat_id=chat.id).exists():
        ChatMember.objects.create(
            user_id=user.id,
            chat_id=chat.id,
            is_admin=False
        )
        return JsonResponse({
        'chat': {
            'title': chat.title,
            'description': chat.description,
            'users': serialize_users_json(chat),
            'admins': serialize_admins_json(chat)
        }
    })
    return JsonResponse({}, status=400)


@require_http_methods(['DELETE'])
def del_chat_member(request):
    body = json.loads(request.body)
    chat = get_object_or_404(Chat, id=body.get('chat_id'))
    user = get_object_or_404(User, id=body.get('user_id'))

    ChatMember.objects.filter(user_id=user.id, chat_id=chat.id).delete()
    return JsonResponse({'deletion': True})


@require_http_methods(['DELETE'])
def del_chat(request):
    body = json.loads(request.body)
    chat = get_object_or_404(Chat, id=body.get('id'))
    chat.delete()
    return JsonResponse({'deletion': True})


@require_http_methods(['GET'])
def show_chat_info(request):
    chat = get_object_or_404(Chat, id=request.GET['id'])
    return JsonResponse({
        'chat': {
            'title': chat.title,
            'description': chat.description,
            'creator': str(chat.creator),
            'category': str(chat.category),
            'users': serialize_users_json(chat),
            'admins': serialize_admins_json(chat)
        }
    })


@require_http_methods(['PATCH'])
def add_chat_admin(request):
    body = json.loads(request.body)
    chat = get_object_or_404(Chat, id=body.get('chat'))
    user = get_object_or_404(User, id=body.get('user'))

    chat_member = get_object_or_404(
        ChatMember, chat_id=chat.id, user_id=user.id, is_admin=False)
    chat_member.is_admin = True
    chat_member.save()

    return JsonResponse({
        'chat': {
            'title': chat.title,
            'description': chat.description,
            'creator': str(chat.creator),
            'category': str(chat.category),
            'users': serialize_users_json(chat),
            'admins': serialize_admins_json(chat)
        }
    })


@require_http_methods(['PATCH'])
def del_chat_admin(request):
    body = json.loads(request.body)
    chat = get_object_or_404(Chat, id=body.get('chat'))
    user = get_object_or_404(User, id=body.get('user'))

    chat_member = get_object_or_404(
        ChatMember, chat_id=chat.id, user_id=user.id, is_admin=True)
    chat_member.is_admin = False
    chat_member.save()

    return JsonResponse({
        'chat': {
            'title': chat.title,
            'description': chat.description,
            'creator': str(chat.creator),
            'category': str(chat.category),
            'users': serialize_users_json(chat),
            'admins': serialize_admins_json(chat)
        }
    })
