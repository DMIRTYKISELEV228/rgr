# Generated by Django 4.2.1 on 2023-05-21 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hockey', '0016_remove_trener_idplayer'),
    ]

    operations = [
        migrations.AddField(
            model_name='trener',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]
