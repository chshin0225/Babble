# Generated by Django 3.1.1 on 2020-09-16 02:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diaries', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diary',
            old_name='baby_id',
            new_name='baby',
        ),
        migrations.RenameField(
            model_name='diary',
            old_name='creator_id',
            new_name='creator',
        ),
        migrations.RenameField(
            model_name='diary',
            old_name='modifier_id',
            new_name='modifier',
        ),
        migrations.RenameField(
            model_name='diarycomment',
            old_name='diary_id',
            new_name='diary',
        ),
        migrations.RenameField(
            model_name='diarycomment',
            old_name='user_id',
            new_name='user',
        ),
    ]
