# Generated by Django 4.1.7 on 2023-04-25 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='branch_closing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(max_length=200)),
                ('jan', models.CharField(max_length=200)),
                ('feb', models.CharField(max_length=200)),
                ('mar', models.CharField(max_length=200)),
                ('apr', models.CharField(max_length=200)),
                ('may', models.CharField(max_length=200)),
                ('jun', models.CharField(max_length=200)),
                ('jul', models.CharField(max_length=200)),
                ('aug', models.CharField(max_length=200)),
                ('sep', models.CharField(max_length=200)),
                ('oct', models.CharField(max_length=200)),
                ('nov', models.CharField(max_length=200)),
                ('dec', models.CharField(max_length=200)),
                ('flag', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='guest_code',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('br1_guest_code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.CharField(max_length=100)),
                ('emp_name', models.CharField(max_length=250)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=30)),
                ('role', models.CharField(max_length=20)),
                ('emp_branch', models.CharField(max_length=200)),
                ('emp_description', models.TextField()),
                ('user_flage', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='pg1_new_beds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roon_no', models.IntegerField()),
                ('room_name', models.CharField(max_length=100)),
                ('bed_no', models.IntegerField()),
                ('created_by', models.CharField(max_length=100)),
                ('bed_code', models.IntegerField()),
                ('guest_code', models.IntegerField()),
                ('guest_join_date', models.CharField(max_length=50)),
                ('guest_join_month', models.CharField(max_length=50)),
                ('guest_vacated_date', models.CharField(max_length=50)),
                ('guest_vacate_month', models.CharField(max_length=50)),
                ('share_type', models.IntegerField()),
                ('name', models.CharField(max_length=150)),
                ('advance', models.CharField(max_length=15)),
                ('monthly_rent', models.CharField(max_length=12)),
                ('self_mob', models.CharField(max_length=12)),
                ('age', models.IntegerField(null=True)),
                ('remark', models.CharField(max_length=100)),
                ('narration', models.CharField(max_length=250)),
                ('parent_name', models.CharField(max_length=200)),
                ('parent_mob', models.BigIntegerField(null=True)),
                ('permanent_address', models.TextField()),
                ('jan_rent', models.FloatField(null=True)),
                ('jan_advance', models.CharField(max_length=200)),
                ('jan_due_amt', models.CharField(max_length=200)),
                ('jan_rent_rec_date', models.CharField(max_length=200)),
                ('jan_rent_flag', models.IntegerField()),
                ('feb_rent', models.FloatField()),
                ('feb_advance', models.CharField(max_length=200)),
                ('feb_due_amt', models.CharField(max_length=200)),
                ('feb_rent_rec_date', models.CharField(max_length=200)),
                ('feb_rent_flag', models.IntegerField()),
                ('march_rent', models.FloatField()),
                ('march_advance', models.CharField(max_length=200)),
                ('march_due_amt', models.CharField(max_length=200)),
                ('march_rent_rec_date', models.CharField(max_length=200)),
                ('march_rent_flag', models.IntegerField()),
                ('april_rent', models.FloatField()),
                ('april_advance', models.CharField(max_length=200)),
                ('april_due_amt', models.CharField(max_length=200)),
                ('april_rent_rec_date', models.CharField(max_length=200)),
                ('april_rent_flag', models.IntegerField()),
                ('may_rent', models.FloatField()),
                ('may_advance', models.CharField(max_length=200)),
                ('may_due_amt', models.CharField(max_length=200)),
                ('may_rent_rec_date', models.CharField(max_length=200)),
                ('may_rent_flag', models.IntegerField()),
                ('june_rent', models.FloatField()),
                ('june_advance', models.CharField(max_length=200)),
                ('june_due_amt', models.CharField(max_length=200)),
                ('june_rent_rec_date', models.CharField(max_length=200)),
                ('june_rent_flag', models.IntegerField()),
                ('july_rent', models.FloatField()),
                ('july_advance', models.CharField(max_length=200)),
                ('july_due_amt', models.CharField(max_length=200)),
                ('july_rent_rec_date', models.CharField(max_length=200)),
                ('july_rent_flag', models.IntegerField()),
                ('auguest_rent', models.FloatField()),
                ('auguest_advance', models.CharField(max_length=200)),
                ('auguest_due_amt', models.CharField(max_length=200)),
                ('auguest_rent_rec_date', models.CharField(max_length=200)),
                ('auguest_rent_flag', models.IntegerField()),
                ('sept_rent', models.FloatField()),
                ('sept_advance', models.CharField(max_length=200)),
                ('sept_due_amt', models.CharField(max_length=200)),
                ('sept_rent_rec_date', models.CharField(max_length=200)),
                ('sept_rent_flag', models.IntegerField()),
                ('october_rent', models.FloatField()),
                ('october_advance', models.CharField(max_length=200)),
                ('october_due_amt', models.CharField(max_length=200)),
                ('october_rent_rec_date', models.CharField(max_length=200)),
                ('october_rent_flag', models.IntegerField()),
                ('nov_rent', models.FloatField()),
                ('nov_advance', models.CharField(max_length=200)),
                ('nov_due_amt', models.CharField(max_length=200)),
                ('nov_rent_rec_date', models.CharField(max_length=200)),
                ('nov_rent_flag', models.IntegerField()),
                ('dec_rent', models.FloatField()),
                ('dec_advance', models.CharField(max_length=200)),
                ('dec_due_amt', models.CharField(max_length=200)),
                ('dec_rent_rec_date', models.CharField(max_length=200)),
                ('dec_rent_flag', models.IntegerField()),
                ('flag', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='pg1_new_guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roon_no', models.IntegerField()),
                ('room_name', models.CharField(max_length=100)),
                ('bed_no', models.IntegerField()),
                ('created_by', models.CharField(max_length=100)),
                ('bed_code', models.IntegerField()),
                ('guest_code', models.IntegerField()),
                ('guest_join_date', models.CharField(max_length=50)),
                ('guest_join_month', models.CharField(max_length=50)),
                ('guest_vacated_date', models.CharField(max_length=50)),
                ('guest_vacate_month', models.CharField(max_length=50)),
                ('share_type', models.IntegerField()),
                ('name', models.CharField(max_length=150)),
                ('advance', models.CharField(max_length=15)),
                ('monthly_rent', models.CharField(max_length=12)),
                ('self_mob', models.CharField(max_length=12)),
                ('age', models.IntegerField(null=True)),
                ('remark', models.CharField(max_length=100)),
                ('narration', models.CharField(max_length=250)),
                ('parent_name', models.CharField(max_length=200)),
                ('parent_mob', models.BigIntegerField(null=True)),
                ('permanent_address', models.TextField()),
                ('jan_rent', models.FloatField()),
                ('jan_advance', models.CharField(max_length=200)),
                ('jan_due_amt', models.CharField(max_length=200)),
                ('jan_rent_rec_date', models.CharField(max_length=200)),
                ('jan_rent_flag', models.IntegerField()),
                ('feb_rent', models.FloatField()),
                ('feb_advance', models.CharField(max_length=200)),
                ('feb_due_amt', models.CharField(max_length=200)),
                ('feb_rent_rec_date', models.CharField(max_length=200)),
                ('feb_rent_flag', models.IntegerField()),
                ('march_rent', models.FloatField()),
                ('march_advance', models.CharField(max_length=200)),
                ('march_due_amt', models.CharField(max_length=200)),
                ('march_rent_rec_date', models.CharField(max_length=200)),
                ('march_rent_flag', models.IntegerField()),
                ('april_rent', models.FloatField()),
                ('april_advance', models.CharField(max_length=200)),
                ('april_due_amt', models.CharField(max_length=200)),
                ('april_rent_rec_date', models.CharField(max_length=200)),
                ('april_rent_flag', models.IntegerField()),
                ('may_rent', models.FloatField()),
                ('may_advance', models.CharField(max_length=200)),
                ('may_due_amt', models.CharField(max_length=200)),
                ('may_rent_rec_date', models.CharField(max_length=200)),
                ('may_rent_flag', models.IntegerField()),
                ('june_rent', models.FloatField()),
                ('june_advance', models.CharField(max_length=200)),
                ('june_due_amt', models.CharField(max_length=200)),
                ('june_rent_rec_date', models.CharField(max_length=200)),
                ('june_rent_flag', models.IntegerField()),
                ('july_rent', models.FloatField()),
                ('july_advance', models.CharField(max_length=200)),
                ('july_due_amt', models.CharField(max_length=200)),
                ('july_rent_rec_date', models.CharField(max_length=200)),
                ('july_rent_flag', models.IntegerField()),
                ('auguest_rent', models.FloatField()),
                ('auguest_advance', models.CharField(max_length=200)),
                ('auguest_due_amt', models.CharField(max_length=200)),
                ('auguest_rent_rec_date', models.CharField(max_length=200)),
                ('auguest_rent_flag', models.IntegerField()),
                ('sept_rent', models.FloatField()),
                ('sept_advance', models.CharField(max_length=200)),
                ('sept_due_amt', models.CharField(max_length=200)),
                ('sept_rent_rec_date', models.CharField(max_length=200)),
                ('sept_rent_flag', models.IntegerField()),
                ('october_rent', models.FloatField()),
                ('october_advance', models.CharField(max_length=200)),
                ('october_due_amt', models.CharField(max_length=200)),
                ('october_rent_rec_date', models.CharField(max_length=200)),
                ('october_rent_flag', models.IntegerField()),
                ('nov_rent', models.FloatField()),
                ('nov_advance', models.CharField(max_length=200)),
                ('nov_due_amt', models.CharField(max_length=200)),
                ('nov_rent_rec_date', models.CharField(max_length=200)),
                ('nov_rent_flag', models.IntegerField()),
                ('dec_rent', models.FloatField()),
                ('dec_advance', models.CharField(max_length=200)),
                ('dec_due_amt', models.CharField(max_length=200)),
                ('dec_rent_rec_date', models.CharField(max_length=200)),
                ('dec_rent_flag', models.IntegerField()),
                ('flag', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='room_pg1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roon_no', models.IntegerField()),
                ('room_name', models.CharField(max_length=100)),
                ('share_type', models.IntegerField()),
                ('created_by', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.CharField(max_length=10)),
            ],
        ),
    ]
