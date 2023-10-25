from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from deposit.models import DepositModel
from withdraw.models import WithdrawModel

def home(request):
    return render(request,"home.html")


def add(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        uemail = request.POST.get("email")
        upassword = request.POST.get("password")
        ufirst_name = request.POST.get("first_name")
        ulast_name = request.POST.get("last_name")
        uis_staff = request.POST.get("is_staff")
        
        
        # Corrected line: Use the actual password provided by the user
        obj = User.objects.create_user(username=uname, email=uemail, password=upassword,first_name=ufirst_name,last_name=ulast_name,is_staff=uis_staff)
        obj.save()
        return redirect("/account/add")
    else:
        return render(request, "form.html")
    


def loginuser(request):
    if request.method == "POST":
        uname = request.POST.get("uname")
        pswd = request.POST.get("upassword")
        user = authenticate(request, username=uname, password=pswd)
        # upassword=pswd=password
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            d = {"msg": "Invalid username and password"}
            return render(request, "login.html", d)
        

    else:
        return render(request, "login.html")
        
def logot(request):
    logout(request)
    return redirect("/")
#data is deleted when u use logoutrediert function from workbench  

def srch(request):
    uid=request.session.get("_auth_user_id")
    #it takes primery key
    obj=User.objects.get(id=uid)
    srchdata=request.GET.get('srch')
    datad=DepositModel.objects.filter(deposit_description__contains=srchdata,user=obj)
    #filter is giving a particular data
    dataw=WithdrawModel.objects.filter(withdraw_description__contains=srchdata,user=obj)
    #contain work like="%s%"
    
    d={
        "data1": datad,
        "data2": dataw,
        

    }
    return render(request,"srch.html",d)
    

# session key is a pswd
# Create your views here.
  
    
    
    
    
        


    
   
