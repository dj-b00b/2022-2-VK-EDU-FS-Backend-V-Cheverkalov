# Generated by Django 4.1.3 on 2022-11-16 15:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chats_messages', '0004_alter_userreaction_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userreaction',
            name='message',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_userreactions', to='chats_messages.message', verbose_name='Сообщение'),
        ),
        migrations.AlterField(
            model_name='userreaction',
            name='reaction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reaction_userreactions', to='chats_messages.reaction', verbose_name='Реакция'),
        ),
        migrations.AlterField(
            model_name='userreaction',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_userreactions', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
