from django.urls import path
from . import views

urlpatterns = [
    path("",views.getData),
    path("post",views.postData),
    path("get/items",views.getDataItem),
    path("add/items",views.addItem),
]