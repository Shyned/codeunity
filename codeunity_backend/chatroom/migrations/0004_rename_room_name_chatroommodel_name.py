# Generated by Django 4.1.3 on 2022-11-26 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatroom', '0003_remove_chatroommodel_youtube_video_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chatroommodel',
            old_name='room_name',
            new_name='name',
        ),
    ]
