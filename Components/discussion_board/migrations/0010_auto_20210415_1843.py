# Generated by Django 3.0.5 on 2021-04-16 01:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discussion_board', '0009_auto_20210328_1151'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_on', '-num_vote_up']},
        ),
        migrations.AlterModelOptions(
            name='reply',
            options={'ordering': ['-num_vote_up']},
        ),
    ]