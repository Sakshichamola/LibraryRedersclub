# Generated by Django 5.1.6 on 2025-03-28 10:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0010_rename_user_cartitem_reader_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='reader_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.readeruser'),
        ),
    ]
