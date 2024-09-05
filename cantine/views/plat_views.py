from django.shortcuts import render, redirect
from django.contrib import messages
from cantine.models.plat_model import Plat
from cantine.forms import PlatForm


def index(request):
    plats = Plat.objects.all()
    context = {'plats': plats}
    return render(request, 'plats.html', context )
    
def add_plat(request):
    if request.method == 'POST':
        plat_form = PlatForm(request.POST)
        print(0)
        if plat_form.is_valid():
            print(0)
            plat_form.save()
            messages.success(request, 'Plat ajouté')
            return redirect('plat:index')
        else:
            plat_form = PlatForm()
            messages.error(request, 'Plat non ajouté')
            
    plat_form = PlatForm()
    context = {'plat_form': plat_form,
                   'title': 'Ajouter un plat'}
    return render(request, "forms.html", context)
    
def update_plat(request, id):
    plat = Plat.objects.get(id=id)
    if request.method == 'POST':
        plat_form = PlatForm(request.POST, instance=plat)
        if plat_form.is_valid():
            plat_form.save()
            messages.success(request, 'Plat modifié')
            return redirect('plat:index')
        else:
            plat_form = PlatForm(instance=plat)
            messages.error(request, 'Plat non modifié')
            
    plat_form = PlatForm()
    context = {'plat_form': plat_form,
                   'title': 'Ajouter un plat'}
    return render(request,"forms.html", context)

def delete_plat(request, id):
    plat = Plat.objects.get(id=id)
    plat.delete()
    messages.success(request, 'Plat supprimé')
    return redirect('plat:index')