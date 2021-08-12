# Generated by Django 3.2.4 on 2021-08-02 15:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aidApp', '0012_alter_feedback_response_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='marital_status',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='sex',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='app_date',
            field=models.DateField(default=datetime.date(2021, 8, 2)),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='response_type',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='patient',
            name='D_O_B',
            field=models.DateField(default=datetime.date(2021, 8, 2)),
        ),
    ]