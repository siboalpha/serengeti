from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .filters import Search

from .models import Customers
from .forms import CustomersForm


# Create your views here.

def dashboard(request):
    customers = Customers.objects.all()
    customers_search = Search(request.GET, queryset=customers)
    customers = customers_search.qs
    context = {'customers': customers, 'customers_search': customers_search}
    return render(request, 'cms/dashboard.html', context)


def addCustomer(request):
    form = CustomersForm()
    if request.method == 'POST':
        form = CustomersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'cms/add-customer.html', context)


def editCustomer(request, pk):
    customer = Customers.objects.get(id=pk)
    form = CustomersForm(instance=customer)

    if request.method == 'POST':
        form = CustomersForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'cms/add-customer.html', context)


def deleteCustomer(request, pk):
    customer = Customers.objects.get(id=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('/')
    context = {'customer': customer}
    return render(request, 'cms/delete-customer.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'cms/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')
