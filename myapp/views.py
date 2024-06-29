from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm
def login_action(request):
    global email, password
    if request.method == "POST":
        d = request.POST
        for key, value in d.items():
            if key == "email":
                email = value
            if key == "password":
                password = value
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Your Data Got Saved !")
        else:
            return HttpResponse("Failed To Save Data !")
    else:
        form = LoginForm()
    return render(request, 'myapp/login.html', {'form' : form})

#Dictionary Will Be In {}
#Line 5 -> It Works Like A Dictionary In Python, It Store Value Like In Age
#          {"Sachin" : 45, "Peter" : 50}      
#          {"Key"    : Value} -> {"email" : "abc@gmail.com", "password" : "123"}