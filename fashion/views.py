from django.shortcuts import render,redirect
from .form import UserForm
from .models import User
def dashboard(request):
    return render(request,"index.html")

def user_page(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(user_page)
    else:
        form = UserForm()
    users = User.objects.all()

    return render(request,"user.html",{
        "form":form,
        "users":users
    })