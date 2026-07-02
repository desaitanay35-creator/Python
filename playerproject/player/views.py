from django.shortcuts import render,redirect,get_object_or_404
from player.models import PlayersDetails

# Create your views here.
def home(request):
    search= request.GET.get('search')
    if search:
        player= PlayersDetails.objects.filter(name__icontains=search)
    elif (search==" "):
        player=PlayersDetails.objects.all()
    else:
        player=PlayersDetails.objects.all()

    

     
    
    return render(request,'home.html',{'player':player})
def welcome(request):
    return render(request,'welcome.html')
def add(request):
   if request.method=="POST":
        name= request.POST['name']
        test_innings=request.POST['test_innings']
        runs=request.POST['runs']
        PlayersDetails.objects.create(name=name,test_innings=test_innings,runs=runs)
        return redirect('home')
   return render(request,'add.html')

def update(request,id):
    play= get_object_or_404(PlayersDetails,id=id)
    if request.method=='POST':
        play.name=request.POST['name']
        play.test_innings=request.POST['test_innings']
        play.runs=request.POST['runs']
        play.save()

        return redirect('home')
    return render(request,'edit.html',{'play':play})
def dlt(request,id):
    play=get_object_or_404(PlayersDetails,id=id)
    play.delete()
    return redirect('home')
