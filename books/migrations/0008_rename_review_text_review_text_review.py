# Generated by Django 5.1.5 on 2025-02-12 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_remove_review_name_review_stars'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='review_text',
            new_name='text_review',
        ),
    ]
