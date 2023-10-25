from django.urls import path
from .import views as v

urlpatterns = [
    
    
    path("/add",v.add, name='add'),
    path("/loginuser",v.loginuser,name='log'),
    path("/Logout",v.logot,name='logot'),
    path("/Search",v.srch,name="srch")
    #name is short name form of path/maybe view
    
      
    

  
]