from django.shortcuts import render
from basic.models import Destination

def home(request):
    
    dests=Destination.objects.all()
    print(dests[0].img)
    
    context={
        "names":"Mumbai"
    }
    return render(request,"base.html",context)
