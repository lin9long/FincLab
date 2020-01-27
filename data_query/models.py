from django.db import models

# Create your models here.
class FincRBuySellD(models.Model):
    id = models.BigAutoField(primary_key=True)
    ts_code = models.CharField(max_length=64, blank=True, null=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    buy_price_finial = models.DecimalField(max_digits=30, decimal_places=2, blank=True, null=True)
    industry = models.CharField(max_length=64, blank=True, null=True)
    diff_close = models.DecimalField(max_digits=30, decimal_places=2, blank=True, null=True)
    low = models.DecimalField(max_digits=30, decimal_places=2, blank=True, null=True)
    high = models.DecimalField(max_digits=30, decimal_places=2, blank=True, null=True)
    close = models.DecimalField(max_digits=30, decimal_places=2, blank=True, null=True)
    diff_lg_elg_amount = models.DecimalField(max_digits=30, decimal_places=2, blank=True, null=True)
    roll_return_flag = models.DecimalField(max_digits=30, decimal_places=2, blank=True, null=True)
    back_test_win_flag = models.DecimalField(max_digits=30, decimal_places=2, blank=True, null=True)
    buy_price_3 = models.DecimalField(max_digits=30, decimal_places=2, blank=True, null=True)
    buy_price_5 = models.DecimalField(max_digits=30, decimal_places=2, blank=True, null=True)
    back_test_win_gmean = models.DecimalField(max_digits=30, decimal_places=2, blank=True, null=True)
    back_test_win_label = models.BigIntegerField(blank=True, null=True)
    buy_price = models.DecimalField(max_digits=30, decimal_places=2, blank=True, null=True)
    r_sell = models.DecimalField(max_digits=30, decimal_places=2, blank=True, null=True)
    dt = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'finc_r_buy_sell_d'