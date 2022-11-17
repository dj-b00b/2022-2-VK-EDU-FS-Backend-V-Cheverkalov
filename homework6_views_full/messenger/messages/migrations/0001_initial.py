# Generated by Django 4.1.3 on 2022-11-14 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sent_at', models.DateTimeField(auto_now_add=True, verbose_name='Отправлено в')),
                ('content', models.TextField(verbose_name='Содержание сообщения')),
                ('is_readed', models.BooleanField(default=False, verbose_name='Прочитано сообщение')),
                ('is_editing', models.BooleanField(default=False, verbose_name='Отредактировано сообщение')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
        migrations.CreateModel(
            name='Reaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(max_length=15, verbose_name='Вид реакции')),
            ],
            options={
                'verbose_name': 'Реакция',
                'verbose_name_plural': 'Реакции',
            },
        ),
        migrations.CreateModel(
            name='UserReaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Время')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fafaas', to='chats_messages.message', verbose_name='Сообщение')),
                ('reaction', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='afasaf', to='chats_messages.reaction', verbose_name='Реакция')),
            ],
        ),
    ]