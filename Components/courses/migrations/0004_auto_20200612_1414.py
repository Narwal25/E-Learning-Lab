# Generated by Django 3.0.5 on 2020-06-12 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_courses_completion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
