

from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import DepositModel





def adddep(request):
  if request.method=="POST":  
    amt=request.POST.get("amt")
    type=request.POST.get("type")
    date=request.POST.get("date")
    day=request.POST.get("day")
    description=request.POST.get("description")
    uid=request.session.get("_auth_user_id")
    #it tsakes user id from auth_user
    #it takes id of 
    obj=User.objects.get(id=uid)


    objd=DepositModel()
    objd.deposit_amount=amt
    objd.deposit_type=type
    objd.deposit_date=date
    objd.deposit_day=day
    objd.deposit_description=description
    objd.user=obj
    objd.save()
    return redirect("/")
  #for backtend

  else:
    print(request.session.items())
    return render(request,"deposit.html")
  
  
  
def list(request):
  uid=request.session.get("_auth_user_id")
  obj=User.objects.get(id=uid)
  data=DepositModel.objects.filter(user=obj)
  #use for some particular data u want filter
  d={
      "data":data
  }
  return render(request,"depdetails.html",d)
#for frontend







# Create your views here.
