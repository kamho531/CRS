from django.urls import path
from . import views

urlpatterns = [
    path('addcustomers/', views.addcustomers, name="addcustomers"),
    path('updatecustomers/<int:pk>', views.updatecustomers, name="updatecustomers"),
    path('deletecustomers/<int:pk>', views.deletecustomers, name='deletecustomers'),
    path('searchcustomer/', views.searchcustomers, name="searchcustomers"),


]