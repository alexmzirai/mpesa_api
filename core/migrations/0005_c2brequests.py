# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-06 20:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20171105_0354'),
    ]

    operations = [
        migrations.CreateModel(
            name='C2bRequests',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('transaction_type', models.CharField(blank=True, max_length=20, null=True)),
                ('transaction_id', models.CharField(blank=True, max_length=20, null=True)),
                ('transaction_date', models.DateTimeField(blank=True, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True)),
                ('business_short_code', models.CharField(blank=True, max_length=20, null=True)),
                ('bill_ref_number', models.CharField(blank=True, max_length=50, null=True)),
                ('invoice_number', models.CharField(blank=True, max_length=50, null=True)),
                ('org_account_balance', models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True)),
                ('third_party_trans_id', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.BigIntegerField(blank=True, null=True)),
                ('first_name', models.CharField(blank=True, max_length=50, null=True)),
                ('middle_name', models.CharField(blank=True, max_length=50, null=True)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('is_validated', models.BooleanField(default=False)),
                ('is_completed', models.BooleanField(default=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'C2B Requests',
                'db_table': 'tbl_c2b_requests',
            },
        ),
    ]
