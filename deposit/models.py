from django.db import models
from django.contrib.auth.models import User


class DepositModel(models.Model):
    deposit_amount=models.IntegerField()
    deposit_type=models.CharField(max_length=30)
    deposit_description=models.TextField(max_length=30)
    deposit_day=models.CharField(max_length=30)
    deposit_date=models.DateField()
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name="deposit")
    
    
    
    # user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name="expense")
    
    class Meta:
        db_table="deposit"
        
    def __str__(s):
        return s.user.username        
    

# Create your models here.
