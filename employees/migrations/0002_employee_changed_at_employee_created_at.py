# Generated by Django 5.0.3 on 2024-03-24 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='changed_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]