# Generated by Django 3.2.6 on 2021-10-08 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trello', '0007_alter_card_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='comment',
        ),
        migrations.AddField(
            model_name='card',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]