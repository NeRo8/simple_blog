# Generated by Django 2.2 on 2019-04-18 10:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190418_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='datePub',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 18, 10, 26, 21, 965984, tzinfo=utc)),
        ),
    ]
