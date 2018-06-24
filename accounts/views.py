from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def signup(request):
    if request.method == 'POST':
        if validationComparePassword(request.POST['password'], request.POST['password-confirmation']):
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', { "message_error": "Username has already been taken."})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'], email=request.POST['email'], password=request.POST['password'])
                login(request, user)
            #return render(request, 'accounts/signup.html', { "message_ok": "{} created".format(user)})
            return redirect('home')
        else:
            return render(request, 'accounts/signup.html', { "message_error": "Password do not match"})
    else:
        return render(request, 'accounts/signup.html')

def validationComparePassword(password1, password2):
    if password1.strip() == password2.strip():
        return True
    else:
        return False


# Create your views here.
def loginview(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST['next'])
            return redirect('home')
        return render(request, 'accounts/login.html', { "message_error": "Username or password does not match."})
    else:
        return render(request, 'accounts/login.html')


def logoutview(request):
    if request.method == 'POST':
        logout(request)
    return redirect('home')
