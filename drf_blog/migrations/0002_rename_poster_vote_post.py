# Generated by Django 4.0 on 2022-03-30 09:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drf_blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vote',
            old_name='poster',
            new_name='post',
        ),
    ]