from django.shortcuts import render
from home.models.home_model import Home
from django.views.generic import ListView
# Create your views here.

class HomeListView(ListView):
    context_object_name = "homes"
    paginate_by = 12
    queryset = Home.objects.all()
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["homes"] = Home.objects.all() 
        return context
