# Generated by Django 5.0.7 on 2024-07-24 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0004_snippet_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='snippet',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]