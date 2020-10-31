# Generated by Django 2.2.2 on 2019-06-27 10:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0003_auto_20190627_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='thumbnail',
            field=models.FileField(default='default.jpg', upload_to='thumbnail'),
        ),
        migrations.AlterField(
            model_name='video',
            name='upload_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='video',
            name='url',
            field=models.FileField(upload_to='videos'),
        ),
    ]
