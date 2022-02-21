from django.shortcuts import render,redirect
from projects.models import prolductdb,cartdb
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    return render(request,"home.html")

def login(request):
    return render(request,"login.html")

def logindata(request):
    if request.method == "POST":
        uname = request.POST.get('username')
        passw = request.POST.get('password')  
        if User.objects.filter(username__contains=uname).exists():
            return redirect(home)
        else:
            return redirect(login)      
        
def addproducts(request):
    return render(request,"addproducts.html")

def prodata(request):
    if request.method == "POST":
        name = request.POST.get('proname')
        price = request.POST.get('proprice')
        desc = request.POST.get('prodesc')
        image = request.FILES['image']
        obj = prolductdb(proname=name,proprize=price,prodesc=desc,proimage=image)
        obj.save()
        return redirect(addproducts)
    
def viewproducts(request):
    data=prolductdb.objects.all()
    return render(request,"viewproducts.html",{'data':data})

def editpro(request,dataid):
    data=prolductdb.objects.filter(id=dataid)
    return render(request,"editpro.html",{'data':data})

def edit(request,dataid):
    if request.method == "POST":
        name = request.POST.get('proname')
        price = request.POST.get('proprice')
        desc = request.POST.get('prodesc')
        image = request.FILES['image']
        prolductdb.objects.filter(id=dataid).update(proname=name,proprize=price,prodesc=desc,proimage=image)
        return redirect(viewproducts)

def delete(request,dataid):
    prolductdb.objects.filter(id=dataid).delete()
    return redirect(viewproducts) 

def shop(request):
    data = prolductdb.objects.all()
    return render(request,"shop.html",{'data':data})

def single(request,dataid):
    data=prolductdb.objects.filter(id=dataid)
    return render(request,"single-product.html",{'data':data})

def addtocart(request):
    if request.method == "POST":
        name = request.POST.get('name')
        price = request.POST.get('price')
        quantity = request.POST.get('quan')
        obj = cartdb(name=name,prize=price,quantity=quantity)
        obj.save()
        return redirect(mycart)

def mycart(request):
    data = cartdb.objects.all()
    return render(request,"cart.html",{'data':data})

def cdelete(request,dataid):
    cartdb.objects.filter(id=dataid).delete()
    return redirect(mycart) 