# Generated by Django 3.2 on 2022-04-28 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_prospect_occupation_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='customer_message_readed',
            field=models.IntegerField(default=0),
        ),
    ]
