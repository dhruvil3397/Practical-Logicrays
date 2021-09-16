from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm

# Create your views here.
def Contact(request):
    if request.method =="POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            mobile = form.cleaned_data["mobile"]
            form.save()

            print(name,email,mobile)

    form = ContactForm()
    return render(request,"myapp/form.html",{"form":form})