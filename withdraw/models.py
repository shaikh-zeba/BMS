from django.db import models
from django.contrib.auth.models import User

class WithdrawModel(models.Model):
    
    
    withdraw_amount=models.IntegerField()
    withdraw_date=models.DateField()
    withdraw_description=models.TextField(max_length=30)
    withdraw_day=models.TextField(max_length=30)
    withdraw_type=models.TextField(max_length=30)
   
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name="withdraw")
    
    
    
    class Meta:
        db_table="withdraw"
        
    def __str__(s):
        return s.user.username     
    


# Create your models here.
