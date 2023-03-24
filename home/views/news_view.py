from django.shortcuts import render
from home.models.newss_model import News
from django.views.generic import ListView
# Create your views here.

class NewsListView(ListView):
    context_object_name = "newss"
    paginate_by = 12
    queryset = News.objects.all()
    template_name = 'news/news.html' 
    #
    #
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["newss"] = News.objects.all() 
        return context

