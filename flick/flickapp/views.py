from django.shortcuts import render,redirect,get_object_or_404,get_list_or_404
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from.models import*
from django.contrib.auth.models import User
from django.contrib import messages
from.models import Payment1



def home_new(request):
    return render(request,'home.html')




from django.contrib.auth import authenticate, login
from .models import Profile

def signup_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        name = request.POST.get('name')
        age = request.POST.get('age')

        # ✅ Make sure age is provided
        if not age:
            return render(request, 'sign-up.html', {'error': 'Age is required'})

        # Step 1: Create user
        user = User.objects.create_user(username=username, password=password, email=email)

        # Step 2: Assign name and age after profile is created by signal
        profile = user.profile
        profile.name = name
        profile.age = age
        profile.save()

        # Step 3: Auto-login user
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('login')  # Or wherever you want

    return render(request, 'sign-up.html')



from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('payment')  # or use 'action' or 'home'
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'login.html')



def terms(request):
    return render(request,'terms-&-cond.html')



def subs(request):
    return render(request,'subscription.html')





from django.contrib.auth.decorators import login_required

@login_required
def profile_view(request):
    print("User:", request.user)
    print("Name:", request.user.profile.name)
    return render(request, 'profile.html')

from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib import messages

def logout_view(request):
    logout(request)
    return redirect('home')  # Change 'login' to wherever you want to redirect after logout









import re

def extract_file_id(link):
    match = re.search(r'/d/([a-zA-Z0-9_-]+)', link)
    return match.group(1) if match else None

def action(request):
    action_movie = adminpanel.objects.filter(action_movie=True)
    for_kids = adminpanel.objects.filter(for_kids=True)
    horror = adminpanel.objects.filter(horror=True)
    malayalam = adminpanel.objects.filter(malayalam=True)
    tamil = adminpanel.objects.filter(tamil=True)
    feelgood = adminpanel.objects.filter(feelgood=True)
    family = adminpanel.objects.filter(family=True)
    comedy = adminpanel.objects.filter(comedy=True)
    fantasy = adminpanel.objects.filter(fantasy=True)
    crime_thriller = adminpanel.objects.filter(crime_thriller=True)
    survival_movie = adminpanel.objects.filter(survival_movie=True)
    adventure = adminpanel.objects.filter(adventure=True)
    science_fiction = adminpanel.objects.filter(science_fiction=True)

    # Add embed link to each movie
    for movie in list(action_movie) + list(for_kids) + list(horror)+ list(feelgood)+ list(family)+ list(comedy)+ list(fantasy)+ list(crime_thriller)+ list(survival_movie)+ list(adventure)+ list(science_fiction)+ list(malayalam)+ list(tamil):
        if movie.drive_link:
            file_id = extract_file_id(movie.drive_link)
            movie.embed_link = f"https://drive.google.com/file/d/{file_id}/preview"
        else:
            movie.embed_link = None

    return render(request, 'home_2.html', {
        'movie': action_movie,
        'kids': for_kids,
        'horror': horror,
        'feelgood':feelgood,
        'family':family,
        'comedy':comedy,
        'fantasy':fantasy,
        'crime_thriller':crime_thriller,
        'survival_movie':survival_movie,
        'adventure':adventure,
        'science_fiction':science_fiction,
        'malayalam':malayalam,
        'tamil':tamil
    })






     





from django.shortcuts import render
from .forms import *

# def pay(request):
#     if request.method == 'POST':
#         form = Payment1Form(request.POST)
#         if form.is_valid():
#             form.save()
#             return render(request, 'payment.html', {'form': Payment1Form(), 'success': True})
#     else:
#         form = Payment1Form()
#     return render(request, 'payment.html', {'form': form})

from django.shortcuts import render, redirect
from .forms import Payment1Form
from django.contrib import messages

def pay(request):
    if request.method == 'POST':
        form = Payment1Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Payment successful!")
            return redirect('action')  # Avoid resubmission on refresh
        else:
            messages.error(request, "Form is invalid. Please check your input.")
            print(form.errors)  # Debug print
    else:
        form = Payment1Form()
    return render(request, 'payment.html', {'form': form})
