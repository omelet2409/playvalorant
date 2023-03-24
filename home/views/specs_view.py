from django.shortcuts import render
from home.models.specs_model import Spec
from django.views.generic import ListView
# Create your views here.

class SpecsListView(ListView):
    context_object_name = "specs"
    paginate_by = 12
    queryset = Spec.objects.all()
    template_name = 'specs/specs.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["specs"] = Spec.objects.all() 
        return context