from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from accountapp.models import Profile
from .forms import ProfileForm, LoginForm


def sample(request):
    return render(request, 'login.html')


def my_name(request):
    my_name = Profile.objects.filter(id='1').first().name
    return render(request, 'my-name.html', context={
        'name': my_name,
    })


def order_list(request):
    order_list = [
        {'id': 1, 'name': 'Banana', 'price': 100},
        {'id': 2, 'name': 'Mie Ayam', 'price': 200},
        {'id': 3, 'name': 'Nasi Goreng', 'price': 300}
    ]
    return render(request, 'order-list.html', context={
        'order_list': order_list,
        'name': 'John Doe'
    })


def profile(request, user_id):
    if not Profile.objects.filter(id=user_id).exists():
        return render(request, 'profile-not-found.html')

    profile = Profile.objects.get(id=user_id)
    return render(request, 'profile.html', context={
        'name': profile.user.first_name,
        'email': profile.user.email,
        'phone': profile.phone,
        'house_name': profile.house_name,
        'street': profile.street,
        'landmark': profile.landmark,
        'pincode': profile.pincode,
        'city': profile.city,
        'state': profile.state,
        'country': profile.country,
    })


def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = Profile.objects.update_or_create()
            profile.save()
            return redirect('profile', user_id=profile.id)
        else:
            return render(request, 'create-profile.html', context={
                'form': form
            })
    else:
        form = ProfileForm()
    return render(request, 'create-profile.html', context={
        'form': form
    })


def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile', user_id=user.profile.id)
            else:
                return render(request, 'login.html', context={
                    'form': form,
                    'error': 'Invalid username or password'
                })
        else:
            return render(request, 'login.html', context={
                'form': form,
                'error': 'Invalid username or password'
            })
    else:
        form = LoginForm()
        return render(request, 'login.html', context={
            'form': form
        })