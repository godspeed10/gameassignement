# Generated by Django 4.1.3 on 2023-02-10 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_alter_game_new_string'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='num',
            field=models.IntegerField(default=0, max_length=10),
        ),
    ]
