# Generated by Django 5.1.6 on 2025-02-25 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_job_title_alter_customuser_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='about_me',
            field=models.CharField(blank=True, max_length=1500),
        ),
        migrations.AddField(
            model_name='customuser',
            name='age',
            field=models.PositiveIntegerField(default=18),
        ),
    ]
