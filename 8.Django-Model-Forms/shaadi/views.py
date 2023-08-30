from django.shortcuts import render, redirect
from .models import Profile
from .forms import*

# Create your views here.
def ProfileListView(request):
    profiles= Profile.objects.all()
    return render(request, 'shaadi/profile_list.html', {'profiles':profiles})


def ProfileDetailView(request, profile_id):
    profile=Profile.objects.get(id=profile_id)
    return render(request, 'shaadi/profile_detail.html', {'profile': profile})

def ProfileDeleteView(request, profile_id):
    profile=Profile.objects.get(id=profile_id)
    profile.delete()
    profiles= Profile.objects.all()
    return render(request, 'shaadi/profile_detail.html', {'profile': profiles})

def ContactView(request):
    if request.method == 'POST':
        form= ContactForm(request.POST)
        if form.is_valid():
            print(f"Name:{form.cleaned_data['name']}")
            print(f"Email:{form.cleaned_data['email']}")
            print(f"Message:{form.cleaned_data['message']}")
    else:
        form= ContactForm()
    return render(request, 'shaadi/contact.html', {'form':form})

def NewProfileView(request):
    if request.method == 'POST':
        form= ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()    ## only work in modelforms
            return redirect('shaadi:profile_list')
    else:
        form= ProfileForm()
    return render(request, 'shaadi/new_profile.html', {'form':form})