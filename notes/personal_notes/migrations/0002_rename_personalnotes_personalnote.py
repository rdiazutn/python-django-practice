# Generated by Django 4.2.2 on 2023-06-22 02:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personal_notes', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PersonalNotes',
            new_name='PersonalNote',
        ),
    ]