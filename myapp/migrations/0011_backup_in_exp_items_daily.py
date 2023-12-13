# Generated by Django 4.1.7 on 2023-08-12 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_accounts_book_ub_flag_category_ub_flag_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='backup_in_exp_items_daily',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entry_id', models.CharField(max_length=200)),
                ('particulars', models.CharField(max_length=200)),
                ('amount', models.FloatField()),
                ('ledger', models.CharField(max_length=200)),
                ('accounts_book_name', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=200)),
                ('item_catergory', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('day', models.CharField(max_length=200)),
                ('month', models.CharField(max_length=200)),
                ('year', models.CharField(max_length=200)),
                ('enter_by', models.CharField(max_length=200)),
                ('cb_date', models.CharField(max_length=200)),
                ('updated_by', models.CharField(max_length=200)),
                ('ub_date', models.CharField(max_length=200)),
                ('deleted_by', models.CharField(max_length=200)),
                ('db_date', models.CharField(max_length=200)),
                ('ub_flag', models.IntegerField()),
                ('flag', models.IntegerField()),
            ],
        ),
    ]
