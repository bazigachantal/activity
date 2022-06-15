import imp

from django.shortcuts import render
from study.models import Bursary  
# create your views here.
def index(request):
       age = Bursary.objects.all
       size = {'age': age, }
       return render(request,'index.html', size)

def detail(request):
       age = Bursary.objects.all
       sz = {'age': age, }
       return render(request,'detail.html', sz)
                                          
 

