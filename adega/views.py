from django.shortcuts import render
from django.http import HttpResponse
from .models import Adega
from .forms import AdegaForm

# Create your views here.
def home(request):
    adegas = Adega.objects.all()
    contexto = {}
    contexto['adegas'] = adegas
    return render(request, 'adega/home.html', contexto)

def adega_criar(request):
    if request.method == 'POST':
        form = AdegaForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = AdegaForm()
    return render(request, 'adega/adega-criar.html', {'form': form})