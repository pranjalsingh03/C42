from django.contrib import admin
from .models import *
# Register your models here.

admin.site.site_header = 'BharatMobiles'
admin.site.site_title = 'BharatMobiles'
admin.site.register(products)
admin.site.register(staf)
admin.site.register(attendence)
admin.site.register(category)
admin.site.register(notes)
admin.site.register(customer)
admin.site.register(invoice)
admin.site.register(paymenthistory)
admin.site.register(sellhistory)
admin.site.register(shopopen)
admin.site.register(report_history)
admin.site.register(invoice_template)
