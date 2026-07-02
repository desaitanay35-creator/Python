from django.shortcuts import render,get_object_or_404
from player.models import Players
# Create your views here.
def home(request):
    all_player=Players.objects.all()
    return render(request,'home.html',{'pla':all_player})
def about(request):
    return render(request,'about.html')
def navebar(request):
    return render(request,'navebar.html')
def info(request,id):
    play=get_object_or_404(Players,id=id)
    return render(request,'info.html',{'play':play})