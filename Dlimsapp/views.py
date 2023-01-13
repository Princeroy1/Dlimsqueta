
# Create your views here.
from django.shortcuts import render,redirect
from .models import Client
from django.contrib import messages
from .forms import admindata,adminsignup
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    if request.method =='POST':
        my_cnic=request.POST['search']
        mydata=Client.objects.filter(cnic=my_cnic).values()
       
        print(mydata) 
        
        # if not mydata:
        #  messages.error(request, 'Document deleted.')
        return render(request,'search.html',{'data':mydata})
    else:
     return render(request,'index.html')
    
def search(request):
    if request.method=='GET':
        my_cnic=request.GET.get('search')
        mydata=Client.objects.filter(cnic=my_cnic)
       
        # if not mydata:
        #  messages.error(request, 'Document deleted.')
        return render(request,'search.html',{'data':mydata})
    else:
     mydata='Client.objects.filter(cnic=my_cnic).values()'
    return render(request,'search.html')
    
@login_required(login_url='/login/')
def adminpage(request):
    
     data=Client.objects.all().order_by('-issue_date')
     return render(request,'adminpage.html',{'data':data})
    
 
def signin(request):
 if not request.user.is_authenticated:
    if request.method=='POST':
     fm=AuthenticationForm(request=request,data=request.POST)
     if fm.is_valid():
         name=fm.cleaned_data['username']
         passw=fm.cleaned_data['password']
         
         user=authenticate(username=name,password=passw)
         if user is not None:
            login(request,user)
            return HttpResponseRedirect('/adminpage/')
    else:
        fm=AuthenticationForm()
    return render(request,'login.html',{'form':fm})
 else:
    return HttpResponseRedirect('/adminpage/')

def signup(request):
  if not request.user.is_authenticated:
    if request.method=='POST':
     fm=adminsignup(request.POST)
     if fm.is_valid():
          fm.save()
          messages.success(request, 'Account created successfully')
          return redirect('/signin/')
    else:
       fm=adminsignup() 
    return render(request,'signup.html',{'form':fm})
  else:
      return redirect('/adminpage/')
@login_required(login_url='/login/')
def delete(request,id):
    if request.method=='POST':
        Pi=Client.objects.get(pk=id)
        Pi.delete()
    return HttpResponseRedirect('/adminpage/')
  
@login_required(login_url='/login/')
def edit(request,id):
    if request.method=='POST':
       pi=Client.objects.get(pk=id)
       fm=admindata(request.POST,instance=pi)
       if fm.is_valid():
           fm.save()
        #    return render(request,'Files/edit.html',{'form':fm})
           return redirect('/adminpage/')
    else: 
       pi=Client.objects.get(pk=id)
       fm=admindata(instance=pi)
    return render(request,'edit.html',{'form':fm})
 
@login_required(login_url='/login/')
def Ad(request):
    if request.method=='POST':
        fm=admindata(request.POST , request.FILES )
        if fm.is_valid():
         pic=fm.cleaned_data['pic']
         cnic=fm.cleaned_data['cnic']
         Licence_number=fm.cleaned_data['Licence_number']
         Driver_name=fm.cleaned_data['Driver_name']
         Father_name=fm.cleaned_data['Father_name']
         Allowed_Vehcial=fm.cleaned_data['Allowed_Vehcial']
         state=fm.cleaned_data['state']
         city=fm.cleaned_data['city']
         issue_date=fm.cleaned_data['issue_date']
         valid_from=fm.cleaned_data['valid_from']
         valid_to=fm.cleaned_data['valid_to']
        #  qr_code=(f"http://127.0.0.1:8000/search/?search={cnic}")
        #  qr=qrcode.make(qr_code)
        #  qr.save(str(cnic)+'.png')

         reg=Client(pic=pic,cnic=cnic,Licence_number=Licence_number,Driver_name=Driver_name,
                     Father_name=Father_name,Allowed_Vehcial=Allowed_Vehcial,state=state,city=city,issue_date=issue_date
,valid_from=valid_from,valid_to=valid_to)
       
         reg.save()
        #  messages.success(request, 'Data Saved Success')
         return redirect('/adminpage/')
    else:
        fm=admindata()
    return render(request,'Add.html',{'form':fm})
@login_required(login_url='/login/')
def find(request):
    search_post = request.GET.get('find')
    if search_post:
     posts = Client.objects.filter(cnic=search_post)
    else:
        posts=messages.error(request,'NOT FOUND')
    return render(request,'find.html',{'post':posts})

@login_required(login_url='/login/')
def logot(request):
    
 logout(request)
 return HttpResponseRedirect('/login/')