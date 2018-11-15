from django.shortcuts import render, redirect, get_object_or_404
from .models import Client
from .forms import ClientForm
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request, 'accounts/home.html', {})

def home_admin(request):
    return render(request, 'accounts/home_admin.html', {})

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'accounts/client_list.html', {'clients': clients})


def register(request):
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ClientForm()
    return render(request, 'accounts/register.html', {'form': form})


def edit(request, pk):
    client = get_object_or_404(Client, pk=pk)
    if request.method == "POST":
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm(instance=client)
    return render(request, 'accounts/edit.html', {'form': form})

def delete(request, pk):
    Client.objects.filter(cliente=pk).delete()
    return redirect('client_list')