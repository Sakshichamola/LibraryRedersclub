# Generated by Django 5.1.6 on 2025-03-25 09:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0005_rename_title_autocar_name_rename_title_business_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='autocar',
            old_name='name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='business',
            old_name='name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='comic',
            old_name='name',
            new_name='tile',
        ),
        migrations.RenameField(
            model_name='competitive_exam',
            old_name='name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='entertainment',
            old_name='name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='fashion',
            old_name='name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='fitness',
            old_name='name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='health',
            old_name='name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='holiday',
            old_name='name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='lifestyles',
            old_name='name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='magazine',
            old_name='name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='new_arrivals',
            old_name='name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='newspaper',
            old_name='name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='popular',
            old_name='name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='sport',
            old_name='name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='technology',
            old_name='name',
            new_name='tile',
        ),
    ]
