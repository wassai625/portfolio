# Generated by Django 4.1.3 on 2022-12-10 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_favoriteforcomment_timestamp_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postcomment',
            old_name='comment_date',
            new_name='comment_data',
        ),
    ]