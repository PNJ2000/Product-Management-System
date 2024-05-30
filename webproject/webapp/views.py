from django.shortcuts import render, redirect
from webapp.models import CustomUser, Users
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from webapp.forms import CustomForm, UsersForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

def signup(request):
    us = request.POST['user_username']
    pa = request.POST['user_password'] 
    use= User.objects.create_user(username=us ,password=pa)
    CustomUser.objects.filter(user=use).update(add=request.POST['user_add'],phone_no=request.POST['user_phoneno'],dob=request.POST['user_dob'])
    return render(request, "login.html")

def userLogin(request):
    if request.method == 'POST':
        name = request.POST['username_log']
        passw = request.POST['userpass_log']
        verify = authenticate(request, username=name, password=passw)
        if verify:  
            login(request,verify)  
            return redirect('/homepage')
        else:
            error_message = "Invalid Username or Password."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request,"login.html")
    
def login_page(request):
    return render(request,"login.html")

def signup_page(request):
    return render(request,"signup.html")

@login_required(login_url="/")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def homepage(request):
    return render(request, "homepage.html", {})

def logout_view(request):
    logout(request)
    return render(request,"login.html")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def productlog(request):
    if request.method == "POST":
        form = UsersForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                pass
    else:
        form = UsersForm()
    return render(request, "productlog.html",{'form':form})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def show(request):
    users=Users.objects.all()
    return render(request,'show.html',{'users':users})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def edit(request, id):  
    user = Users.objects.get(id=id)  
    return render(request,'edit.html', {'user':user})  
 

def update(request, id):  
    user = Users.objects.get(id=id)  
    form = UsersForm(request.POST, instance = user)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'user': user})  

  
def destroy(request, id):  
    user = Users.objects.get(id=id)  
    user.delete()  
    return redirect("/show")

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def userdata(request):
    db= CustomUser.objects.all()
    return render(request,"userdata.html",{"db":db})

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def edituser(request, id):
    us = User.objects.get(id = id)
    return render(request,"edituser.html",{'us':us})

def deluser(request, id):       
        u = User.objects.get(id = id)
        u.delete()
        return redirect("/userdata")

def updateuser(request,user_id):
     # Retrieve the User instance to update
    user = User.objects.get(pk=user_id)
    
    # Retrieve the associated CustomUser instance
    cu = CustomUser.objects.get(user=user)
    
    if request.method == 'POST':
        # Create a form instance with the POST data
        form = CustomForm(request.POST, instance=cu)
        
        if form.is_valid():
            # Update the User model fields
            user.username = form.cleaned_data['username']
            user.set_password(form.cleaned_data['password'])
            user.save()
            
            # Update the CustomUser model fields
            cu.add = form.cleaned_data['add']
            cu.dob = form.cleaned_data['dob']
            cu.phone_no = form.cleaned_data['phone_no']
            cu.save()
            
            # Redirect to a success page or any other page
            return redirect('/userdata')
    else:
        # Populate the form with initial data from the models
        form = CustomForm(instance=cu)
    
    return render(request, 'userdata.html', {'form': form})
    