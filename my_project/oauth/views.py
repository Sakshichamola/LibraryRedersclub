from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm

def custom_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("user_dashboard")  # Redirect to home page
        else:
            return render(request, "oauth/login.html", {"error": "Invalid credentials"})

    return render(request, "oauth/login.html")

def signup_view(request):
    if request.method == 'POST':
        full_name = request.POST.get('signup_name')
        username = request.POST.get('signup_username')
        email = request.POST.get('signup_email')
        password = request.POST.get('signup_password')
        ref_code = request.POST.get('signup_ref')

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('signup')

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('signup')

        # Create new user
        user = User.objects.create_user(username=username, email=email, password=password)
        # user.first_name = full_name  # Save full name as first name
        user.save()

        messages.success(request, "Account created successfully. You can now log in.")
        return redirect('login')  # Redirect to login page

    return render(request, 'oauth/signup.html')  # Render signup page for GET request


def logout_view(request):
    logout(request)
    return redirect("user_dashboard")

def profile(request):
    return render(request, 'profile.html')

def settings(request):
    return render(request, 'settings.html')

def purchase_history(request):
    return render(request, 'purchase_history.html')

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("user_dashboard")  # Redirect after signup
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {"form": form})





