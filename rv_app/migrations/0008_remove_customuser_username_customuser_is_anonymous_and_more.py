# Generated by Django 4.2 on 2023-04-12 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rv_app', '0007_customuser_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='username',
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_anonymous',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_authenticated',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]