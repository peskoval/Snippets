# Generated by Django 5.0.7 on 2024-07-25 16:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0007_remove_snippet_status_snippet_public_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1000)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('snippet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='MainApp.snippet')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
