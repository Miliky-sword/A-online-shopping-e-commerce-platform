# Generated by Django 3.1.7 on 2021-06-01 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_loginuser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loginuser',
            name='password',
            field=models.CharField(max_length=999),
        ),
    ]
