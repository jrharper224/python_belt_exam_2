from django.shortcuts import render, redirect
from .models import *
import datetime

# Create your views here.
def index(request):
    return render(request, 'belt/index.html')

def travels(request):
    context = {
    'trips': Trip.objects.all()
    }

    return render(request, 'belt/success.html', context)

def add_trip(request):
    return render(request, 'belt/trip.html')

def destinations(request, id):
    context = {
        'id': id,
        'destination': Trip.objects.get(id = id),
    }
    return render(request, 'belt/destinations.html', context)

def user_trips(request):

    return redirect('/travels')

def login_user(request):
    login = User.objects.login_user(request.POST)
    if login[0]:
        request.session['name'] = login[1].name
        return redirect('/travels')
    return redirect('/')


def create_user(request):
    #used to validate and create a new user
    if User.objects.validate_user(request.POST):
        user = User.objects.create(
            name = request.POST.get('name'),
            username = request.POST.get('username'),
            password = bcrypt.hashpw(request.POST.get('password').encode(), bcrypt.gensalt()),
        )
        request.session['user_id'] = user.id
        request.session['name'] = user.name
        return redirect('/travels')
    return redirect('/')

def create_trip(request):
    #used to validate and create a new trip from the add trip form
    if Trip.objects.validate_trip(request.POST):
        trip = Trip.objects.create(
            destination = request.POST.get('destination'),
            description = request.POST.get('description'),
            travel_start = request.POST.get('travel_start'),
            travel_end = request.POST.get('travel_end'),
        )
        return redirect('/travels')
    return redirect('/add')

def logout(request):
    request.session.clear()
    return redirect('/')
