# Generated by Django 3.2.4 on 2021-10-18 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aidApp', '0009_alter_appointment_app_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='health_practitioner',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to='aidApp.health_practitioner'),
            preserve_default=False,
        ),
    ]
