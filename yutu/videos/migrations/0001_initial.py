# Generated by Django 3.0 on 2019-12-06 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('verbose_name', models.CharField(max_length=30)),
                ('visibility', models.BooleanField(default=True)),
                ('rated', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('video', models.FileField(default='default.mp3', upload_to='uploads/videos/%Y/%m/%d/')),
            ],
        ),
    ]