from django.urls import path

from . import views

urlpatterns =[
    path('',views.mobiles , name = "mobiles" ),
    path('save_mobile/',views.save_mobile , name = "save_mobile" ),
    path('delete_mobile/',views.delete_mobile , name = "delete_mobile" )
]