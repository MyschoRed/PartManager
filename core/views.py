from django.http import QueryDict
from django.shortcuts import render, get_object_or_404

from django.views import View
from core.forms import CustomerForm, PartForm
from core.models import Part, Customer


class HomeView(View):
    template_name = 'core/home.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


def customer_list(request):
    customers = Customer.objects.all()
    form = CustomerForm()
    ctx = {
        'customers': customers,
        'form': form
    }
    return render(request, 'core/customers_list.html', ctx)


def customer_add(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST or None)
        if form.is_valid():
            customer = form.save()
            ctx = {'customer': customer}
            return render(request, 'core/customer_detail.html', ctx)
    return render(request, 'core/customer_add.html', {'form': CustomerForm()})


def customer_delete(request, pk):
    customer = Customer.objects.get(pk=pk)
    customer.delete()
    customers = Customer.objects.all()
    return render(request, 'core/customers_list.html', {'customers': customers})


def customer_edit(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    form = CustomerForm(instance=customer)

    ctx = {
        'customer': customer,
        'form': form
    }
    if request.method == 'GET':
        return render(request, 'core/customer_edit.html', ctx)
    elif request.method == 'PUT':
        data = QueryDict(request.body).dict()
        form = CustomerForm(data, instance=customer)
        if form.is_valid():
            form.save()
            return render(request, 'core/customers_list.html', ctx)


def part_list(request):
    parts = Part.objects.all()
    form = PartForm()
    ctx = {
        'parts': parts,
        'form': form
    }
    return render(request, 'core/parts_list.html', ctx)


def part_add(request):
    if request.method == 'POST':
        form = PartForm(request.POST or None)
        if form.is_valid():
            part = form.save()
            ctx = {'part': part}
            return render(request, 'core/part_detail.html', ctx)
    return render(request, 'core/part_add.html', {'form': PartForm()})


def part_delete(request, pk):
    part = Part.objects.get(pk=pk)
    part.delete()
    parts = Part.objects.all()
    return render(request, 'core/customers_list.html', {'parts': parts})


def part_edit(request, pk):
    part = get_object_or_404(Part, pk=pk)
    form = PartForm(instance=part)

    ctx = {
        'part': part,
        'form': form
    }
    if request.method == 'GET':
        return render(request, 'core/part_edit.html', ctx)
    elif request.method == 'PUT':
        data = QueryDict(request.body).dict()
        form = PartForm(data, instance=part)
        if form.is_valid():
            form.save()
            return render(request, 'core/parts_list.html', ctx)