from django.shortcuts import render,redirect
from django.contrib.auth import  authenticate, login, logout
from django.contrib import  messages
from .forms import SignUpForm, AddRecordForm
from .models import Record
from django.forms.models import model_to_dict




# Create your views here.
def home(request):
    records = Record.objects.all()
    
    if request.method == 'POST':
        username = request.POST['username']
        password =  request.POST['password']
        
        # Authenticate
        user =  authenticate(request, username=username, password = password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "You have been  logged in.")
            return redirect('home')
        else:
            messages.success(request, "There was an error")
            return redirect('home')
    return render(request, 'home.html', {'records':records})

# def login_user(request):
#     pass

def  register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered..")
            return redirect('home')
    
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    
    return render(request, 'register.html', {'form':form})


def  logout_user(request):
    logout(request)
    messages.success(request, "You're  logged  out")
    return redirect('home')   


def customer_record(request,  pk):
    if request.user.is_authenticated:
        customer_record  = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record':customer_record})
    else:
        messages.success(request, "You must be  loggged in to  view  the  record")
        return redirect('home')           

        

def  delete_customer_record(request,  pk):
    if request.user.is_authenticated:
        delete_customer = Record.objects.get(id=pk)
        delete_customer.delete()
        messages.success(request, "Your record is  deleted..")
        return  redirect('home')
    else:
        messages.success(request, "You must be loggged in to delete the  record")
        return redirect('home')          
    
    
def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "Record Added...")
                return redirect('home')
        return render(request, 'add_record.html', {'form':form})
    else:
        messages.success(request, "You must be loggged in to add record")
        return redirect('home')           
 
 
def update_customer_record(request, pk):
    if request.user.is_authenticated:
        targeted_record  = Record.objects.get(id=pk)
        form = AddRecordForm(request.POST or None, instance= targeted_record)
        if form.is_valid():
            if form.has_changed():  # Check if the form data has changed
                form.save()
                messages.success(request, "This record is updated")
                return redirect('home')
            else:
                messages.info(request, "You have not changed anything")
                
        return render(request, 'update_record.html', {'form':form})
            
        
     
 