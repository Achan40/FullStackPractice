from django.shortcuts import render
# class based views
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from . import models

from django.urls import reverse_lazy

# Create your views here.
# Template class based views
class IndexView(TemplateView):
    template_name = 'index.html'

    # Injecting conent (kwargs gives all keyword arguments except for corresponsing parameter as a dictionary)
    # User defined parameters as a dictionary
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = 'BASIC INJECTION'
        return context

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = models.School

class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = models.School

    # points to template\basic_app folder under basic_app folder
    template_name = 'basic_app/school_detail.html'

class SchoolCreateView(CreateView):
    fields = ('name','principal','location')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields = ('name','principal')
    model = models.School

class SchoolDeleteView(DeleteView):
    model = models.School
    success_url =  reverse_lazy("basic_app:list")