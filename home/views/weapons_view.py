from django.shortcuts import render
from home.models.weapons_model import Weapon
from django.views.generic import ListView
# Create your views here.

class WeaponListView(ListView):
    context_object_name = "weapons"
    paginate_by = 12
    queryset = Weapon.objects.all()
    template_name = 'weapon/weapon.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["weapons"] = Weapon.objects.all() 
        return context
