# Generated by Django 3.0.4 on 2020-04-12 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20200411_0216'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='is_send',
            field=models.BooleanField(default=False),
        ),
    ]
