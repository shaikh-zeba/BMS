from django.contrib import admin

from .models import DepositModel

class DepositSchema(admin.ModelAdmin):
    list_display=['id','user','deposit_amount','deposit_type','deposit_description','deposit_date']

admin.site.register(DepositModel,DepositSchema)
# Register your models here.
