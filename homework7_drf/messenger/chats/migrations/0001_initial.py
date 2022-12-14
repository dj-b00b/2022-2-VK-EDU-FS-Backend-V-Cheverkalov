# Generated by Django 4.1.3 on 2022-11-22 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название категории')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название чата')),
                ('description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Описание чата')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создан в')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='static/', verbose_name='Аватар чата')),
            ],
            options={
                'verbose_name': 'Чат',
                'verbose_name_plural': 'Чаты',
            },
        ),
        migrations.CreateModel(
            name='ChatMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_admin', models.BooleanField(verbose_name='Администратор')),
                ('adding_time', models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_chatmembers', to='chats.chat', verbose_name='Чат')),
            ],
            options={
                'verbose_name': 'Участник чата',
                'verbose_name_plural': 'Участники чата',
            },
        ),
    ]
