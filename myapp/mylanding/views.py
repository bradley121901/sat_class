from django.shortcuts import render, redirect
from .forms import register_form, login_form
import pymongo
connection_string = "mongodb+srv://truebliu:D5MLAfLxaFMTOia1@cluster0.a74k35z.mongodb.net/?retryWrites=true&w=majority"

def home(request):
    if request.method == "GET":
        return render(request, "home.html")
    if request.method == "POST":
        if "Register" in request.POST:
            return redirect(f'/registerpage')
        if "Login" in request.POST:
            return redirect(f'/loginpage')
'''

    username = forms.CharField(label="username", max_length=30)
    password = forms.CharField(label="password", max_length=30)
    firstname = forms.CharField(label="firstname", max_length=30)
    lastname = forms.CharField(label="lastname", max_length=30)
    email = forms.CharField(label="email", max_length=30)
    '''

def register(request):
    if request.method == "GET":
        form = register_form()
        return render(request, "register.html", {"form": form})
    if request.method == "POST":
        if "Register" in request.POST:
            form = register_form(request.POST)
            if form.is_valid():
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password"]
                firstname = form.cleaned_data["firstname"]
                lastname = form.cleaned_data["lastname"]
                email = form.cleaned_data["email"]
                
                document = {"username": username, "password":password, "firstname": firstname, "lastname": lastname, "email": email}
        
                client = pymongo.MongoClient(connection_string)
                db = client["Cluster0"]
                collection = db["Cluster0"]
                collection.insert_one(document)
                client.close()
                return redirect(f'/')
            else:
                return render(request, "register.html", {"form": form})

def login(request):
    if request.method == "GET":
        form = login_form()
        return render(request, "login.html", {"form":form})
    if request.method == "POST":
        if "Login" in request.POST:
            form = login_form(request.POST)
            if form.is_valid():
                username = form.cleaned_data["username"]
                password = form.cleaned_data["password"]
                
                document = {"username":username, "password":password}
                client = pymongo.MongoClient(connection_string)
                db = client["Cluster0"]
                collection = db["Cluster0"]
                flag = collection.find_one(document)
                client.close()
                if flag:
                    return redirect(f'/')
                else:
                    return redirect(f'/loginpage')
                
        
    