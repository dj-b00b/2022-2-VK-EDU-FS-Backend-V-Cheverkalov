from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from users.models import User, UserSession, Contact
from django.shortcuts import get_object_or_404
import json
# Create your views here.


@require_http_methods(['GET'])
def get_info_about_user(request):
    user = get_object_or_404(User, id=request.GET['id'])
    return JsonResponse({
        'user': {
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'about_user': user.about_user,
            'phone_number': user.phone_number,
            'avatar': str(user.avatar)
        }
    })


@require_http_methods(['PUT'])
def change_info_about_user(request):
    body = json.loads(request.body)
    user = get_object_or_404(User, id=body.get('id'))

    for field, value in body.items():
        setattr(user, field, value)
        user.save()

    return JsonResponse({
        'user': {
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'about_user': user.about_user,
            'phone_number': user.phone_number,
            'avatar': str(user.avatar)
        }
    })


@require_http_methods(['GET'])
def show_list_contacts(request):
    user = get_object_or_404(User, id=request.GET['id'])

    list_contacts = []
    contacts = Contact.objects.filter(user_id=user.id)
    for contact in contacts:
        list_contacts.append({
            'user_id': str(contact.user),
            'name': contact.name,
            'surname': contact.surname,
            'phone_number': contact.phone_number,
            'friend': str(contact.friend)
        })


@require_http_methods(['POST'])
def add_user_to_contacts(request):
    user = get_object_or_404(User, id=request.POST['user'])

    if not User.objects.filter(phone_number=request.POST['phone_number']).exists():
        return JsonResponse({'error': 'The specified user is not registered in the messenger'}, status=400)

    if Contact.objects.filter(phone_number=request.POST['phone_number']).exists():
        return JsonResponse({}, status=400)

    new_contact = Contact.objects.create(
        user_id=user.id,
        name=request.POST['user'],
        surname=request.POST.get('surname', ''),
        phone_number=request.POST['phone_number'],
        friend=User.objects.get(phone_number=request.POST['phone_number'])
    )

    return JsonResponse({
        'user': {
            'username': user.username,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'about_user': user.about_user,
            'phone_number': user.phone_number,
            'avatar': str(user.avatar)
        }
    })


@require_http_methods(['DELETE'])
def del_user_from_contacts(request):
    body = json.loads(request.body)
    user = get_object_or_404(User, id=body.get('user'))
    friend = get_object_or_404(User, id=body.get('friend'))

    contact = get_object_or_404(Contact, user_id=user.id, friend_id=friend.id)
    contact.delete()
    return JsonResponse({"deletion": True})
