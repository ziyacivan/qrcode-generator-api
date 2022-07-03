# Generated by Django 4.0.5 on 2022-07-03 15:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('qrcodes', '0003_remove_qrcode_path_qrcode_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qrcode',
            name='image',
        ),
        migrations.AddField(
            model_name='qrcode',
            name='file',
            field=models.FileField(default=datetime.datetime(2022, 7, 3, 15, 40, 48, 92427, tzinfo=utc), upload_to='qrcodes/images'),
            preserve_default=False,
        ),
    ]