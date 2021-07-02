from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.utils import timezone

# Create your views here.
def index(request):
    return render(request, 'index.html')

def list(request):
    jean = Jean.objects.all()
    return render(request, 'list.html', {'jean':jean})

def detail(request, id):
    jean=get_object_or_404(Jean, pk=id)
    return render(request, 'detail.html', {'jean':jean})

def post_jean(request):
    if request.method=='POST':
        new_jean=Jean()
        new_jean.name=request.POST['name']
        new_jean.price=request.POST['price']
        new_jean.material=request.POST['material']
        new_jean.image=request.FILES.get('image')
        new_jean.save()
        return redirect('list')  
    else: # GET 메소드인 경우
        return render(request, 'post_jean.html')
