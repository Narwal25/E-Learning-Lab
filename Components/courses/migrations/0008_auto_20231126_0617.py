# Generated by Django 3.0.5 on 2023-11-26 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_courses_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='description',
            field=models.TextField(max_length=255),
        ),
    ]
