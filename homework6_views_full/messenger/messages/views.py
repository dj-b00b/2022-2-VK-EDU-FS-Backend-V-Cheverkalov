from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponseNotFound
from chats.models import Chat, ChatMember
from messages.models import Message, Reaction, UserReaction
from users.models import User
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
import json
# Create your views here.


def serialize_reactions_json(obj):
    user_reactions = UserReaction.objects.filter(message_id=obj.id)
    reactions_list = []

    for user_reaction in user_reactions:
        reactions_list.append({
            'reaction': user_reaction.reaction_id,
            'user': user_reaction.user_id,
            'time': user_reaction.time
        })
    return reactions_list


@require_http_methods(['POST'])
def create_message(request):
    message = Message.objects.create(
        chat=Chat.objects.get(id=request.POST['chat_id']),
        sender=User.objects.get(id=request.POST['sender']),
        content=request.POST['content']
    )
    return JsonResponse({
        'message': {
            'chat': str(message.chat),
            'sent_at': message.sent_at,
            'sender': str(message.sender),
            'content': message.content,
            'is_readed': message.is_readed,
            'is_editing': message.is_editing,
            'reactions': serialize_reactions_json(message)
        }
    })


@require_http_methods(['PUT'])
def edit_message(request):
    body = json.loads(request.body)
    message = get_object_or_404(Message, id=body.get('id'))
    try:
        new_content = body.get('content')
    except KeyError:
        return JsonResponse({}, status=400)
    else:
        message.content = new_content
        message.is_editing = True
        message.save()
        return JsonResponse({
            'message': {
                'chat': str(message.chat),
                'sent_at': message.sent_at,
                'sender': str(message.sender),
                'content': message.content,
                'is_readed': message.is_readed,
                'is_editing': message.is_editing,
                'reactions': serialize_reactions_json(message)
            }
        })


@require_http_methods(['PUT'])
def read_message(request):
    body = json.loads(request.body)
    message = get_object_or_404(Message, id=body.get('id'))
    message.is_readed = True
    message.save()
    return JsonResponse({
        'message': {
            'chat': str(message.chat),
            'sent_at': message.sent_at,
            'sender': str(message.sender),
            'content': message.content,
            'is_readed': message.is_readed,
            'is_editing': message.is_editing,
            'reactions': serialize_reactions_json(message)
        }
    })


@require_http_methods(['DELETE'])
def del_message(request):
    body = json.loads(request.body)
    message = get_object_or_404(Message, id=body.get('id'))
    message.delete()
    return JsonResponse({'deletion': True})


@require_http_methods(['GET'])
def show_list_messages(request):
    chat_id = request.GET['id']
    chat = get_object_or_404(Chat, id=chat_id)
    messages = Message.objects.filter(chat_id=chat_id)

    message_list = []
    for message in messages:
        message_list.append({
            'chat': str(message.chat),
            'sent_at': message.sent_at,
            'sender': str(message.sender),
            'content': message.content,
            'is_readed': message.is_readed,
            'is_editing': message.is_editing,
            'reactions': serialize_reactions_json(message)
        })
    return JsonResponse({'messages': message_list})


@require_http_methods(['POST'])
def add_reaction(request):
    message = get_object_or_404(Message, id=request.POST['message_id'])
    reaction = get_object_or_404(Reaction, id=request.POST['reaction_id'])
    user = get_object_or_404(User, id=request.POST['user_id'])

    if UserReaction.objects.filter(user_id=request.POST['user_id'], message_id=request.POST['message_id'],
                                   reaction_id=request.POST['reaction_id']).exists():
        return JsonResponse({}, status=400)

    if UserReaction.objects.filter(user_id=request.POST['user_id'], message_id=request.POST['message_id']).exists():
        UserReaction.objects.get(
            user_id=request.POST['user_id'], message_id=request.POST['message_id']).delete()

    UserReaction.objects.create(
        message_id=message.id,
        reaction_id=reaction.id,
        user_id=user.id
    )

    return JsonResponse({
        'message': {
            'chat': str(message.chat),
            'sent_at': message.sent_at,
            'sender': str(message.sender),
            'content': message.content,
            'is_readed': message.is_readed,
            'is_editing': message.is_editing,
            'reactions': serialize_reactions_json(message)
        }
    })


@require_http_methods(['DELETE'])
def del_reaction(request):
    body = json.loads(request.body)
    message = get_object_or_404(Message, id=body.get('message_id'))
    reaction = get_object_or_404(Reaction, id=body.get('reaction_id'))
    user = get_object_or_404(User, id=body.get('user_id'))

    obj = get_object_or_404(UserReaction, user_id=body.get('user_id'), message_id=body.get('message_id'),
                            reaction_id=body.get('reaction_id'))
    obj.delete()

    return JsonResponse({
        'message': {
            'chat': str(message.chat),
            'sent_at': message.sent_at,
            'sender': str(message.sender),
            'content': message.content,
            'is_readed': message.is_readed,
            'is_editing': message.is_editing,
            'reactions': serialize_reactions_json(message)
        }
    })
