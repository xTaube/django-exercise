# Generated by Django 3.2.4 on 2021-06-30 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='type',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]