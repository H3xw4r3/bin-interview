from django.shortcuts import render, HttpResponse, redirect
from django.db.models import Sum
from .models import AnnouncedPuResult, PollingUnit
from .forms import LgaForm, AddResultForm


# Create your views here.

def puResult(request, pu_id):
    result = AnnouncedPuResult.objects.filter(polling_unit_uniqueid=pu_id)
    context = {
        'result': result,
    }

    return render(request, 'pu_result.html', context)


def index(request):
    polling_units = PollingUnit.objects.all()
    context = {
        'units': polling_units
    }
    return render(request, 'index.html', context)


def lga_result(request):
    form = LgaForm()
    if request.method == 'POST':
        form = LgaForm(request.POST)
        lga_id = request.POST.get('lga')
        polling_units = PollingUnit.objects.filter(lga_id=lga_id)
        print(polling_units)

        total_score = AnnouncedPuResult.objects.filter(
            polling_unit_uniqueid__in=polling_units
        ).aggregate(total_score=Sum('party_score'))['total_score']
        context = {
        'total_score': total_score,
        'polling_units':polling_units,
        }

        return render(request, 'lga_results.html', context)

    context = {
        'form': form,
    }
    return render(request, 'lga_results.html', context)


def addResult(request):
    form = AddResultForm()
    if request.method == "POST":
        form = AddResultForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'add_result.html', {'form':form})


