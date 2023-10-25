from django.urls import path
from .import views as v

urlpatterns = [
      path("/Add",v.adddep,name="add"),
      path("/List",v.list,name="list"),
       
    
    # path("/abc",v.'abc')

  
]