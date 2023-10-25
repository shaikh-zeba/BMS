

from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import WithdrawModel

def addwithdraw(request):
  if request.method=="POST":  
    amt=request.POST.get("amt")
    type=request.POST.get("type")
    date=request.POST.get("date")
    day=request.POST.get("day")
    description=request.POST.get("description")
    uid=request.session.get("_auth_user_id")
    #it takes auth-user id
    obj=User.objects.get(id=uid)


    objw=WithdrawModel()
    # use model from model
    objw.withdraw_amount=amt
    objw.withdraw_type=type
    objw.withdraw_date=date
    objw.withdraw_day=day
    objw.withdraw_description=description
    objw.user=obj
    objw.save()
    return redirect("/")

  else:
    return render(request,"withdraw.html")

  
def list(request):
  uid=request.session.get("_auth_user_id")
  obj=User.objects.get(id=uid)
  data=WithdrawModel.objects.filter(user=obj)
  #use for some particular data want
  #u use filter u see only login person explist and  inclist
  d={
    "data":data
  }
  return render(request,"withdrawdetails.html",d)
  


# Create your views here.
