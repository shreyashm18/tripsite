from django.shortcuts import render
from .models import destination
# Create your views here.
def triphome(request):

    dest1=destination()
    dest1.price=800
    dest1.name='Pune'
    dest1.desc='peshve city never lose'
    dest1.img='destination_4.jpg'

    dest2=destination()
    dest2.price=400
    dest2.name='Mumbai'
    dest2.desc='capital'
    dest2.img='destination_6.jpg'

    dest3=destination()
    dest3.price=700
    dest3.name='delhi'
    dest3.desc='polluted'
    dest3.img='destination_3.jpg'
    dest=[dest1,dest2,dest3]
    return render(request,'index.html',{'Dest':dest})