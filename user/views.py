from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from .forms import UserAdminCreationForm,LoginForm
from .models import User
from evaluate.models import Worker

def register(request):
    form = UserAdminCreationForm(request.POST or None)
    if form.is_valid():
        fin = form.cleaned_data.get("fin")
        username = form.cleaned_data.get("username")
        sirname = form.cleaned_data.get("sirname")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")

        newUser = User(fin = fin, username = username, sirname = sirname, email = email)
        newUser.set_password(password)
        newUser.save()
        
        messages.success(request, "Uğurla qeydiyyatdan keçdiniz!")
        login(request, newUser)

        return redirect("index")
    context = {
        "form" : form
    }
    return render(request, "register.html", context)

def loginUser(request):
    form = LoginForm(request.POST or None)
    context = {
        "form" : form
    }
    if form.is_valid():
        fin = form.cleaned_data.get("fin")
        password = form.cleaned_data.get("password")
        if request.user.is_authenticated:
            return redirect("index")
        user = authenticate(fin = fin, password = password)
        worker = Worker.objects.filter(worker_fin = fin)
        if user is None:
            messages.info(request, "İstifadəçi tapılmadı. Xahiş edirik yenidən cəhd edin!")
            return render(request, "login.html", context)
        messages.success(request, "Sistemə daxil oldunuz!")
        login(request, user)
        if worker != None:
            # context_worker = {"worker" : worker}
            for i in worker:
                if i.is_bm:
                    return redirect("/evaluation_panel/branchmanager")
                elif i.is_as:
                    return redirect("/evaluation_panel/appraisalspecialist")
        return redirect("index")
    return render(request, "login.html", context)

def logoutUser(request):
    logout(request)
    messages.success(request,"Sistemdən çıxış etdiniz!")
    return redirect("index")
