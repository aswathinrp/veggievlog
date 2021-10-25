from django.shortcuts import render

from . models import veg
# Create your views here.
def fun(request):
    obj=veg.objects.all()
    return render(request,'index.html',{'results':obj})