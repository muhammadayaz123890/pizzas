# Generated by Django 4.1.2 on 2023-02-12 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Src_App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='requests',
            field=models.IntegerField(default=0),
        ),
    ]
