# Generated by Django 4.1.7 on 2023-09-29 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branch5app', '0006_share_holders'),
    ]

    operations = [
        migrations.AddField(
            model_name='share_holders',
            name='share_holders_amt',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
    ]
