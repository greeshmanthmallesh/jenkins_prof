from django.shortcuts import render
from django.http import HttpResponse

# Create your  here.
def home(request):
    
    return render(request,'name.html')
def home1(request):
    name = (request.POST['n1'])
    return render(request,'base.html',{'name':name})
def add(request):

    val1 = int(request.POST['gp1'])
    val2 = int(request.POST['gp2'])
    val3 = int(request.POST['gp3'])
    val4 = int(request.POST['gp4'])
    val5 = int(request.POST['gp5'])
    
   

    va1 = float(request.POST['cr1'])
    va2 = float(request.POST['cr2'])
    va3 = float(request.POST['cr3'])
    va4 = float(request.POST['cr4'])
    va5 = float(request.POST['cr5'])

    
    resu = (val1*va1)+(val2*va2)+(val3*va3)+(val4*va4)+(val5*va5)
    cc = va1+va2+va3+va4+va5
    resul = resu/cc

    return render(request,'result.html',{'result':resul})