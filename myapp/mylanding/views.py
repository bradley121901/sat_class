from django.shortcuts import render, redirect
from .forms import register_form
def register(request):
    if request.method == "GET":
        return render(request, "register.html")
    if request.method == "POST":
        if "Complete" in request.POST:
            return redirect(f'/filloutform')

def filloutform(request):
    if request.method == "GET":
        form = register_form()
        return render(request, "fillform.html", {"form": form})
    if request.method == "POST":
        if "Register" in request.POST:
            return redirect(f'/')
    