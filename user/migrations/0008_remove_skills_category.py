# Generated by Django 5.0.1 on 2024-02-09 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_alter_project_technology_alter_project_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skills',
            name='category',
        ),
    ]