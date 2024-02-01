from django.shortcuts import render,redirect
from .models import Member
from .forms import MemberForms,Registerform
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.
def home(request):
    member = Member.objects.all()
    context = {'member':member}
    return render(request,'home.html',context)

def Createmember(request):
    member = MemberForms()
    if request.method == 'POST':
        member = MemberForms(request.POST)
        if member.is_valid():
            member.save() 
            return redirect('home')
    context = {'member':member}
    return render(request,'create.html',context)

def member(request,pk):
    member_room = Member.objects.get(id=pk)
    context = {'member_room':member_room}
    return render(request,'room.html',context)


def about(request):
    return render(request,'about.html',)

def delete_member(request,pk):
    member = Member.objects.get(id=pk)
    member.delete()
    messages.success(request,"Deleted This Member")
    return redirect('home')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return redirect('login')
    

    return render(request,'login.html',{})

def register_user(request):
    form = Registerform()
    if request.method == 'POST':
        form = Registerform(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('home')
        
    return render(request,'register.html',{'form':form})

def logout_user(request):
    logout(request)
    return redirect('home')

def search_member(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        members = Member.objects.filter(name__contains=searched)

    return render(request,'search.html',{'searched':searched,'members':members})