# Generated by Django 3.0.2 on 2020-01-21 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FincRBuySellD',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('ts_code', models.CharField(blank=True, max_length=64, null=True)),
                ('name', models.CharField(blank=True, max_length=64, null=True)),
                ('buy_price_finial', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('industry', models.CharField(blank=True, max_length=64, null=True)),
                ('diff_close', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('low', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('high', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('close', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('diff_lg_elg_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('roll_return_flag', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('back_test_win_flag', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('buy_price_3', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('buy_price_5', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('back_test_win_gmean', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('back_test_win_label', models.BigIntegerField(blank=True, null=True)),
                ('buy_price', models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True)),
                ('dt', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'finc_r_buy_sell_d',
                'managed': False,
            },
        ),
    ]
