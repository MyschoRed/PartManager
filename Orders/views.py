from django.http import QueryDict
from django.shortcuts import render, get_object_or_404

from Orders.forms import OrderForm
from Orders.models import Order



def order_list(request):
    orders = Order.objects.all()
    form = OrderForm()
    ctx = {
        'orders': orders,
        'form': form
    }
    return render(request, 'Orders/orders.html', ctx)


def order_add(request):
    if request.method == 'POST':
        form = OrderForm(request.POST or None)
        if form.is_valid():
            order = form.save()
            ctx = {'order': order}
            return render(request, 'Orders/order_detail.html', ctx)
        else:
            print(form.errors)
    return render(request, 'Orders/order_add.html', {'form': OrderForm()})


def order_delete(request, pk):
    order = Order.objects.get(pk=pk)
    order.delete()
    orders = Order.objects.all()
    return render(request, 'Orders/orders.html', {'orders': orders})


def order_edit(request, pk):
    order = get_object_or_404(Order, pk=pk)
    form = OrderForm(instance=order)

    ctx = {
        'order': order,
        'form': form
    }
    if request.method == 'GET':
        return render(request, 'Orders/order_edit.html', ctx)
    elif request.method == 'POST':
        data = QueryDict(request.body).dict()
        form = OrderForm(data, instance=order)
        if form.is_valid():
            form.save()
            return render(request, 'Orders/orders.html', ctx)


def import_bom(request):
    return render(request, 'Orders/import_bom.html')