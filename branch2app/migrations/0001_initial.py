# Generated by Django 4.1.7 on 2023-04-23 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='br2test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('br2test_name', models.CharField(max_length=10)),
            ],
        ),
    ]
