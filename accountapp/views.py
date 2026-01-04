from django.shortcuts import render, redirect

from accountapp.models import Profile


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


def profile(request, id):
    profile = Profile.objects.get(id=id)
    return render(request, 'profile.html', context={
        'name': profile.name,
        'email': profile.email,
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
        id = request.POST.get('id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        house_name = request.POST.get('house_name')
        street = request.POST.get('street')
        landmark = request.POST.get('landmark')
        pincode = request.POST.get('pincode')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')
        profile = Profile.objects.create(
            id=id, 
            name=name, 
            email=email, 
            phone=phone, 
            house_name=house_name, 
            street=street, 
            landmark=landmark, 
            pincode=pincode, 
            city=city, 
            state=state, 
            country=country,
            role='STUDENT'
        )
        profile.save()
        return redirect('profile', id=id)
    return render(request, 'create-profile.html')