# Generated by Django 5.0.6 on 2024-06-03 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0006_category_description'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='ItemCategory',
        ),
    ]
