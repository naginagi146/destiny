# from destiny.forms import RouletteCreateForm
from django.shortcuts import render
from .models import Roulette, Category
from django.views.generic import ListView, DetailView, CreateView
from .forms import RouletteCreateForm, CategoryCreateForm, ContentFormset
from django.urls import reverse_lazy
from django.db import transaction



class RouletteListView(ListView):
    model = Roulette
    template_name = "destiny/roulette_list.html"
    context_object_name = 'roulettes'
    pagenate_by = 10



class RouletteDetailView(DetailView):
    model = Roulette
    template_name = "destiny/roulette_detail.html"



class RouletteCreateView(CreateView):
    model = Roulette
    template_name = "destiny/roulette_create.html"
    form_class = RouletteCreateForm
    formset = ContentFormset

    def get_context_data(self, **kwargs):
        data = super(RouletteCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            data['formset'] = ContentFormset(self.request.POST)
        else:
            data['formset'] = ContentFormset()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        content_formset = context['formset']

        if content_formset.is_valid():
            with transaction.atomic():
                content_formset.instance = self.object
                content_formset.save()
                self.object = form.save()

        return super(RouletteCreateView, self).form_valid(content_formset)

    def get_success_url(self):
        return reverse_lazy('destiny:roulette_list')




