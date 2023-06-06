from django.http import QueryDict
from django.shortcuts import render, get_object_or_404

from Parts.forms import PartForm
from Parts.models import Part


# Create your views here.
def part_list(request):
    parts = Part.objects.all()
    form = PartForm()
    ctx = {
        'parts': parts,
        'form': form
    }
    return render(request, 'Parts/parts_list.html', ctx)


def part_add(request):
    if request.method == 'POST':
        form = PartForm(request.POST or None)
        if form.is_valid():
            part = form.save()
            ctx = {'part': part}
            return render(request, 'Parts/part_detail.html', ctx)
    return render(request, 'Parts/part_add.html', {'form': PartForm()})


def part_delete(request, pk):
    part = Part.objects.get(pk=pk)
    part.delete()
    parts = Part.objects.all()
    return render(request, 'Parts/parts_list.html', {'parts': parts})


def part_edit(request, pk):
    part = get_object_or_404(Part, pk=pk)
    form = PartForm(instance=part)

    ctx = {
        'part': part,
        'form': form
    }
    if request.method == 'GET':
        return render(request, 'Parts/part_edit.html', ctx)
    elif request.method == 'POST':
        data = QueryDict(request.body).dict()
        form = PartForm(data, instance=part)
        if form.is_valid():
            form.save()
            return render(request, 'Parts/parts_list.html', ctx)

