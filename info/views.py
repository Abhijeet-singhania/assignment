from django.shortcuts import render,redirect
from . import forms
from .models import Items
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

@login_required(login_url="/account/login/")
def home(request):
    
    data = Items.objects.filter(userid=request.user.id).order_by('date')
    # print(request)
    
    return render(request, 'info/index.html' , {"data" : data})

def add_view(request):
    
    
    if request.method == 'POST':
        
        form = forms.CreateItem(request.POST)
        # print(form)
        if form.is_valid():
            # save article to db
            
            instance = form.save(commit=False)
            instance.userid = request.user.id
            # print(instance.status)
            instance.save()
            return redirect('info:home')
    else:
        form = forms.CreateItem()
    return render(request, 'info/add_template.html', { 'form': form })

def edit(request,id):
    data= Items.objects.get(id=id)
    return render(request, 'info/update.html', { 'data': data })

def update(request,id):
    data= Items.objects.get(id=id)
    form = forms.CreateItem(request.POST)
    if form.is_valid():
            instance = form.save(commit=False)
            instance.userid = request.user.id
            # print(instance.status)
            instance.save()
            
            data.delete()
            return redirect('info:home')

    return render(request,'info/update.html',{'data':data})

def remove(request,id):
    data = Items.objects.get(id=id)
    data.delete()
    return redirect('info:home')

def filter_view(request):
    print(request.POST)
    id=request.POST.get('date')
    data = Items.objects.filter(date=id)
    return render(request, 'info/index.html' , {"data" : data})




    
