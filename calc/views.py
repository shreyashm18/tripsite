from django.shortcuts import render

# Create your views here.
def page(request):
    return render(request,'page.html',{'name':'Shreyash'})

def home(request):
   
    return render(request,'home.html',{'name':'Shreyash'})

def result(request):
    text=request.GET['fulltext']
    wrdlst=text.split()
    wrddict={}
    for word in wrdlst:
        if word in wrddict:
            wrddict[word]+=1
        else:
            wrddict[word]=1
    
    return render(request,'result.html',{'Text':text,'Words':wrddict})