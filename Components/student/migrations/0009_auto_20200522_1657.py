# Generated by Django 3.0.5 on 2020-05-22 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_post_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='course_id',
            field=models.CharField(default='None', max_length=255),
        ),
    ]
