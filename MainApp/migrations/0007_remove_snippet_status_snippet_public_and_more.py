# Generated by Django 5.0.7 on 2024-07-25 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0006_alter_snippet_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='snippet',
            name='status',
        ),
        migrations.AddField(
            model_name='snippet',
            name='public',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='lang',
            field=models.CharField(choices=[('py', 'Python'), ('js', 'JavaScript'), ('cpp', 'C++'), ('html', 'HTML')], max_length=30),
        ),
    ]
