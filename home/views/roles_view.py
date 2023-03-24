from django.shortcuts import render
from home.models.roles_model import Role
from django.views.generic import ListView
# Create your views here.

class RoleListView(ListView):
    context_object_name = "roles"
    paginate_by = 12
    queryset = Role.objects.all()
    template_name = 'role/role.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["roles"] = Role.objects.all() 
        return context