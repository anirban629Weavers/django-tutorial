from django.shortcuts import render

# Create your views here.
def home(request):
    # return HttpResponse("<h1>Home</h1>")
    return render(request,"home.html",{'name':"Anirban"})

def addResult(request):
    a=int(request.POST['n1'])
    b=int(request.POST['n2'])
    res=a+b
    print(res)
    return render(request,"result.html",{'ans':res})