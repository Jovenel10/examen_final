
# Create your views here.
from django.shortcuts import render, redirect
from .models import Livre
from .forms import LivreForm

def home(request):
    livres = Livre.objects.all()
    return render(request, 'home.html', {'livres': livres})

def livre(request, livre_id):
    livre = Livre.objects.get(id=livre_id)
    return render(request, 'livre_detail.html', {'livre': livre})

def ajout_livre(request):
    if request.method == 'POST':
        form = LivreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = LivreForm()
    return render(request, 'ajout_livre.html', {'form': form})

def modifier_livre(request, livre_id):
    livre = Livre.objects.get(id=livre_id)
    if request.method == 'POST':
        form = LivreForm(request.POST, instance=livre)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = LivreForm(instance=livre)
    return render(request, 'modifier_livre.html', {'form': form})

def supprimer_livre(request, livre_id):
    livre = Livre.objects.get(id=livre_id)
    if request.method == 'POST':
        livre.delete()
        return redirect('home')
    return render(request, 'supprimer_livre.html', {'livre': livre})
