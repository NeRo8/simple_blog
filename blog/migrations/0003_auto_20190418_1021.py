# Generated by Django 2.2 on 2019-04-18 10:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190418_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='datePub',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 18, 10, 21, 39, 449683, tzinfo=utc)),
        ),
    ]
