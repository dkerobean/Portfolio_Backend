# Generated by Django 5.0.1 on 2024-02-01 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_remove_profile_contact'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tesimonial',
            new_name='Testimonial',
        ),
    ]