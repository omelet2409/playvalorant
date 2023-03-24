from django.shortcuts import render
from home.models.agents_model import Agent
from django.views.generic import ListView
from django.views.generic import DetailView
# Create your views here.

class AgentListView(ListView):
    context_object_name = "agents"
    paginate_by = 12
    queryset = Agent.objects.all()
    template_name = 'agent/agent.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["agents"] = Agent.objects.all() 
        return context

class AgentDetailView(DetailView):
    model = Agent
    template_name = 'agent/agent_detai.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["agent"] = Agent.objects.all() 
        return context

