# Generated by Django 2.0.9 on 2018-12-13 01:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bookclub', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='submitted_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
