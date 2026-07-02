from django.shortcuts import render

# Create your views here.
def Home(request):
    l=[1,2,3,4,5]
    return render(request,'Home.html',{'data':l})
def About(request):
    return render(request,'About.html')

    # l=[]

    