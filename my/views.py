from django.shortcuts import render,redirect
from form.models import data
def home(request):
    if request.method=="POST":
        name=request.POST.get('name')
        data(name=name).save()
        return redirect("/")

    return render(request,"hello.html")

    