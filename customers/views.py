from django.shortcuts import render, redirect
from .models import Customer
from .forms import AddCustomerForm
from django.contrib import messages


# Create your views here.


def addcustomers(request):
    form = AddCustomerForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                addrecord = form.save()
                messages.success(request, "Record saved!")
                return redirect('home')
        return render(request, 'customers/addcustomers.html', {"form": form})
    else:
        messages.success(request, "Must be logged in!")
        return redirect('home')



def updatecustomers(request, pk):
    if request.user.is_authenticated:
        customer = Customer.objects.get(id=pk)
        form = AddCustomerForm(request.POST or None, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, "Record updated!")
            return redirect('home')
        return render(request, 'customers/updatecustomers.html', {"customer": customer, "form": form})       
    else:
        messages.success(request, "Must be logged in!")
        return redirect('home')
    



def deletecustomers(request, pk):
    if request.user.is_authenticated:
        customer = Customer.objects.get(id=pk)
        if request.method == "POST":
            customer.delete()
            messages.success(request, "Record deleted!")
            return redirect('home')
        return render(request, 'customers/deletecustomers.html', {'customer': customer})
    else:
        messages.success(request, "Must be logged in to do that!")
        return redirect('home')



def searchcustomers(request):
    if request.method == "POST":
        searched = request.POST['searched']
        customersfn = Customer.objects.filter(first_name__contains=searched)
        customersln = Customer.objects.filter(last_name__contains=searched)
        return render (request, 'customers/searchcustomers.html',
                        {'searched':searched,
                         'customersfn':customersfn,
                         'customersln':customersln,})
    else:
        return render (request, 'customers/searchcustomers.html',
                        {})
