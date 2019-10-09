
from django.urls import path
from. import views

urlpatterns = [
   path('',views.triphome,name='triphome'),
]
