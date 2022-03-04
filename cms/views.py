from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .filters import Search
from django.db.models import Q

from .models import Customers
from .forms import CustomersForm

from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    customers = Customers.objects.all()
    context = {'customers': customers}
    return render(request, 'cms/dashboard.html', context)


@login_required(login_url='login')
def addCustomer(request):
    form = CustomersForm()
    if request.method == 'POST':
        form = CustomersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'cms/add-customer.html', context)


@login_required(login_url='login')
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


@login_required(login_url='login')
def deleteCustomer(request, pk):
    customer = Customers.objects.get(id=pk)
    if request.method == 'POST':
        customer.delete()
        return redirect('/')
    context = {'customer': customer}
    return render(request, 'cms/delete-customer.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
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


@login_required(login_url='login')
def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def searchCustomer(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        submitbutton = request.GET.get('submit')
        if query is not None:
            lookups = Q(name__icontains=query) | Q(surname__icontains=query) | Q(id__icontains=query)
            results = Customers.objects.filter(lookups).distinct()
            context = {'results': results, 'submitbutton': submitbutton}
            return render(request, 'cms/search.html', context)
        else:
            return render(request, 'cms/search.html')
    else:
        return render(request, 'cms/search.html')
