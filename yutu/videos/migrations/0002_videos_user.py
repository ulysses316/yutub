# Generated by Django 3.0 on 2019-12-07 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_users_image_profile'),
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='videos',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Users'),
        ),
    ]
