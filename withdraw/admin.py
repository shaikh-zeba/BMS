from django.contrib import admin

from .models import WithdrawModel

class WithdrawSchema(admin.ModelAdmin):
    list_display=['id','user','withdraw_amount','withdraw_type','withdraw_description','withdraw_date']

admin.site.register(WithdrawModel,WithdrawSchema)



# Register your models here.
