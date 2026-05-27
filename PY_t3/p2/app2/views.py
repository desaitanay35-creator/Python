from django.shortcuts import render

# Create your views here.
def Contect(request):
    return render(request,'contect.html')
def base(request):
    return render(request,'base.html')
def base(request):
    name='Tanay'
    number=10
    return render(request,'base.html',{'n':name,'fd':number})