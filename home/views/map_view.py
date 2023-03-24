from django.shortcuts import render
from home.models.map_model import Map
from django.views.generic import ListView
# Create your views here.

class MapListView(ListView):
    context_object_name = "maps"
    paginate_by = 12
    queryset = Map.objects.all()
    template_name = 'map/map.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["maps"] = Map.objects.all() 
        return context