# Generated by Django 2.0 on 2018-09-21 11:19

import base.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20180921_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='key',
            name='g',
            field=base.models.BigBigField(),
        ),
        migrations.AlterField(
            model_name='key',
            name='p',
            field=base.models.BigBigField(),
        ),
        migrations.AlterField(
            model_name='key',
            name='x',
            field=base.models.BigBigField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='key',
            name='y',
            field=base.models.BigBigField(),
        ),
    ]