# Generated by Django 4.1.2 on 2023-02-12 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pizzerio_API', '0002_alter_subscription_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='requests_per_day',
            field=models.IntegerField(default=0),
        ),
    ]
