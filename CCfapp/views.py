from django.shortcuts import render, redirect
from . forms import CustomerForm
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'CCfapp/home.html')

def index(request):
    return render(request,'CCfapp/index.html')

def complaint(request):
    form = CustomerForm()
    if request.method == 'POST': 
      if form.is_valid():
          form.save() 
          messages.success(request,("You have successfully registered your complaint!"))
      else: 
          messages.error(request,("Form is not valid"))    
      return redirect('index')
    return render(request,'CCfapp/complaint.html',{'form':form})
