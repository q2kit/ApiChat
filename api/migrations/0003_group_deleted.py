# Generated by Django 4.0.5 on 2022-07-01 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_couple_is_pending_room_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
