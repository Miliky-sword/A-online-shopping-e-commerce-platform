# Generated by Django 3.1.7 on 2021-06-01 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_loginuser_phonenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='loginuser',
            name='sig',
            field=models.CharField(default='There are no personalized signature', max_length=200),
        ),
    ]
