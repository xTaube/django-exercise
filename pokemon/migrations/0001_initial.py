# Generated by Django 3.2.4 on 2021-06-30 19:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import pokemon.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=pokemon.models.upload_status_image)),
                ('updates', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]