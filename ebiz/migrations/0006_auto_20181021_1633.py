# Generated by Django 2.0.7 on 2018-10-21 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebiz', '0005_auto_20181021_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business_info',
            name='paid_permit',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='business_info',
            name='permit_expected',
            field=models.FloatField(),
        ),
    ]