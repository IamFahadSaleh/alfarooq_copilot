# Generated by Django 4.1.7 on 2023-10-06 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_mediabuying_media_amount_dollar'),
    ]

    operations = [
        migrations.AddField(
            model_name='mediabuyingrequests',
            name='media_date_request',
            field=models.DateField(null=True),
        ),
    ]
