from datetime import date
from os import name
from django.db import models
from datetime import datetime

# Create your models here.


class staf(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=20, default='')

    def __str__(self):
        return f"{self.name}"


class category(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=1000, default='')

    def __str__(self):
        return f"{self.name}"


class customer(models.Model):
    id = models.BigAutoField(primary_key=True)
    month = models.CharField(
        max_length=100, default=f"{datetime.now().date().strftime('%B')}", editable=False)
    id2 = models.CharField(max_length=100, default='#CINV00000')
    name = models.CharField(max_length=50, default='')
    address = models.CharField(max_length=200, default='', blank=True)
    contact = models.CharField(max_length=30, default='')
    gst_no = models.CharField(max_length=100, default='', blank=True)
    badge = models.CharField(max_length=200, default='')
    buys = models.CharField(max_length=100, default=0)

    def __str__(self):
        return f"{self.name} | {self.badge}"


class products(models.Model):
    id = models.BigAutoField(primary_key=True)
    month = models.CharField(max_length=100,
                             default=f"{datetime.now().date().strftime('%B')}")
    name = models.CharField(max_length=1000, default='', blank=True)
    category = models.ForeignKey(
        category, on_delete=models.CASCADE, max_length=1000, default='')
    trend = models.CharField(max_length=100, default='0')
    Sale_price = models.IntegerField(default='')
    Buy_price = models.IntegerField(default='')
    stock = models.IntegerField(default='')

    def __str__(self):
        return f"{self.name}- [Available {self.stock}]"


class attendence(models.Model):
    id = models.BigAutoField(primary_key=True)
    staf_name = models.ForeignKey(
        staf, max_length=100, on_delete=models.CASCADE)
    state = models.CharField(max_length=100, choices=(
        ('Present', 'Present'), ('Absent', 'Absent')), default='None')
    date = models.CharField(
        default=f"{datetime.now().date().strftime('%B %d, %Y')}", max_length=100)

    def __str__(self):
        return f"{self.staf_name}- [{self.state}]"


class sellhistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    month = models.CharField(max_length=100,
                             default=f"{datetime.now().date().strftime('%B')}", editable=False)
    date = models.CharField(
        max_length=1000, default=f"{datetime.now().date().strftime('%B %d, %Y')}{datetime.now().time().strftime('%H:%M:%S')}")
    detail = models.CharField(max_length=100, default='Product')
    total = models.CharField(max_length=100, default='0')

    def __str__(self):
        return f"{self.date}"


class notes(models.Model):
    id = models.BigAutoField(primary_key=True)
    date_add = models.CharField(
        max_length=1000, default=f"{datetime.now().date().strftime('%B %d, %Y')}")
    note_body = models.TextField(max_length=10000, default='')

    def __str__(self):
        return f"{self.date_add}"


class paymenthistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    month = models.CharField(max_length=100,
                             default=f"{datetime.now().date().strftime('%B')}", editable=False)
    pay_date = models.CharField(
        max_length=1000, default=f"{datetime.now().date().strftime('%B %d, %Y')}{datetime.now().time().strftime('%H:%M:%S')}")
    staf_name = models.ForeignKey(
        staf, max_length=100, on_delete=models.CASCADE)
    pay = models.CharField(max_length=100, default='')

    def __str__(self):
        return f"{self.staf_name}-[ {self.pay} ]"


class invoice(models.Model):
    month = models.CharField(
        max_length=100, default=f"{datetime.now().date().strftime('%B')}", editable=False)
    order_date = models.CharField(
        max_length=1000, default=f"{datetime.now().date().strftime('%B %d, %Y')} | {datetime.now().time().strftime('%H:%M:%S')}")
    id = models.BigAutoField(primary_key=True)
    id2 = models.CharField(max_length=1000, default='#INV00000')
    customer = models.ForeignKey(customer, on_delete=models.CASCADE)
    order_detail = models.TextField(max_length=1000, default='')
    offer = models.CharField(max_length=100, default='')
    pay_mode = models.CharField(max_length=100, default='Cash')
    total_paid = models.CharField(max_length=100, default='')
    inv_type = models.CharField(max_length=100, default='Normal_Invoice')
    state = models.CharField(max_length=100, choices=(
        ('correct', 'correct'), ('wrong', 'wrong')), default='correct')

    def __str__(self):
        return f"{self.customer} | {self.order_date}"


class shopopen(models.Model):
    id = models.BigAutoField(primary_key=True)
    month = models.CharField(
        max_length=100, default=f"{datetime.now().date().strftime('%B')}", editable=False)
    date = models.CharField(
        max_length=1000, default=f"{datetime.now().date().strftime('%B %d, %Y')}")
    state = models.CharField(max_length=100, choices=(
        ('Open', 'Open'), ('Close', 'Close')), default='None')

    def __str__(self):
        return f"{self.date} | {self.state}"


class report_history(models.Model):
    id = models.BigAutoField(primary_key=True)
    month = models.CharField(
        max_length=100, default=f"{datetime.now().date().strftime('%B')}", editable=False)
    date = models.CharField(
        max_length=1000, default=f"{datetime.now().date().strftime('%B %d, %Y')}")
    customer = models.IntegerField(default=0)
    export = models.IntegerField(default=0)
    imports = models.IntegerField(default=0)
    import_proid = models.TextField(max_length=100000, default='')
    imports_price = models.IntegerField(default=0)
    shop_opend = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.date} | {self.month}"


class invoice_template(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200, default='Invoice-I1')
    header1 = models.TextField(max_length=10000, default='')
    header2 = models.TextField(max_length=10000, default='')
    Footer = models.TextField(max_length=1000000, default='')
    footerlines = models.TextField(max_length=1000000, default='')

    def __str__(self):
        return f"{self.name}"
