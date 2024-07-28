from django.shortcuts import render, redirect
from app.froms import CreateUserFroms, LoginForm, AddRecordForm
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from app.models import Record
from django.contrib import messages


def Home(request):
    return render(request, 'app/index.html')


# Register
def Register(request):
    form = CreateUserFroms()
    if request.method == "POST":
        form = CreateUserFroms(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Created Successfully!")
            return redirect('/login')
    
    context = {'form': form}
    return render(request, 'app/register.html', context = context)


# - Login User
def Login_User(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data= request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password = password)
            if user is not None:
                auth.login(request, user)
                messages.success(request, "You have logged in!!" )
                return redirect("dashboard")
    context = {'form':form}
    return render(request, 'app/login.html', context= context)


# - Dashboard
@login_required(login_url='login')
def Dashboard(request):
    myrecord = Record.objects.all()
    print(myrecord)

    context = {'records': myrecord}

    
    return render(request, 'app/dashboard.html', context=context)

# - Create a record
@login_required( login_url='login')
def Create_record(request):
    form = AddRecordForm()
    if request.method == "POST":
        form = AddRecordForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Your record was created!!!")
            return redirect("dashboard")

    context = {'form':form}
    return render(request, 'app/record.html', context=context)



@login_required(login_url= 'login')
def UpdateRecord(request, pk):
    record = Record.objects.get(id = pk)
    form = AddRecordForm(instance= record)
    if request.method == 'POST':
        form = AddRecordForm(request.POST, request.FILES, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, "Your record was updated!!!")
            return redirect("dashboard")

    context = {'form': form}
    return render(request, 'app/update-record.html', context= context)


# - Read or view singular record
@login_required(login_url='login')
def view_record(request, pk):
    all_records = Record.objects.get(id = pk)


    context = {'record': all_records}
    return render(request, 'app/view-record.html', context= context)


# - Delete a Record

@login_required(login_url= 'login')
def Delete_record(request, pk):
    record = Record.objects.get(id = pk)
    record.delete()
    messages.success(request, "Your record was deleted!!!")
    return redirect("dashboard")


# - User Logout

def Logoutuser(request):
    auth.logout(request)
    messages.success(request, "Logout Success!!!")
    return redirect("login")
 