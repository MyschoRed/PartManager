from django.http import QueryDict
from django.shortcuts import render, get_object_or_404

from Customers.forms import CustomerForm
from Customers.models import Customer


# Create your views here.

def customer_list(request):
    customers = Customer.objects.all()
    form = CustomerForm()
    ctx = {
        'customers': customers,
        'form': form
    }
    return render(request, 'Customers/customers_list.html', ctx)


def customer_preview(request, pk):
    customer = get_object_or_404(Customer, pk=pk)

    ctx = {
        'customer': customer,
    }
    if request.method == 'GET':
        return render(request, 'Customers/customer_preview.html', ctx)


def customer_add(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST or None)
        if form.is_valid():
            customer = form.save()
            ctx = {'customer': customer}
            return render(request, 'Customers/customer_detail.html', ctx)
    return render(request, 'Customers/customer_add.html', {'form': CustomerForm()})


def customer_delete(request, pk):
    customer = Customer.objects.get(pk=pk)
    customer.delete()
    customers = Customer.objects.all()
    return render(request, 'Customers/customers_list.html', {'customers': customers})


def customer_edit(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    form = CustomerForm(instance=customer)

    ctx = {
        'customer': customer,
        'form': form
    }
    if request.method == 'GET':
        return render(request, 'Customers/customer_edit.html', ctx)
    elif request.method == 'PUT':
        data = QueryDict(request.body).dict()
        form = CustomerForm(data, instance=customer)
        if form.is_valid():
            form.save()
            return render(request, 'Customers/customers_list.html', ctx)
