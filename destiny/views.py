# from destiny.forms import RouletteCreateForm
from django.shortcuts import render
from .models import Content, Roulette, Category
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .forms import RouletteCreateForm, CategoryCreateForm, ContentFormset
from django.urls import reverse_lazy
from django.db import transaction
import random
from django.db.models import Q





class RouletteListView(ListView):
    model = Roulette
    template_name = "destiny/roulette_list.html"
    context_object_name = 'roulettes'
    pagenate_by = 10

    def get_queryset(self):
        q_word = self.request.GET.get('query')
        if q_word:
            category_list = Roulette.objects.filter(Q(category__name__icontains=q_word) )
            return category_list
        else:
            return Roulette.objects.all()


class RouletteDetailView(DetailView):
    model = Roulette
    template_name = "destiny/roulette_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contents"] = Content.objects.filter(roulette_id=self.kwargs['pk'])
        return context

class RandomRouletteView(DetailView):
    model = Roulette
    template_name = "destiny/random.html"

    # def get_queryset(self):
    #     queryset = Roulette.objects.all().order_by('?')[:1]
    #     return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contents"] = Content.objects.filter(roulette_id=self.kwargs['pk'])
        return context

class ResultView(DetailView):
    model = Roulette
    template_name = "destiny/result.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contents"] = Content.objects.filter(roulette_id=self.kwargs['pk']).order_by('?')[:1]
        return context






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


class RouletteUpdateView(UpdateView):
    model = Roulette
    template_name = "destiny/roulette_update.html"
    form_class = RouletteCreateForm
    formset = ContentFormset

    def get_context_data(self, **kwargs):
        data = super(RouletteUpdateView, self).get_context_data(**kwargs)
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

        return super(RouletteUpdateView, self).form_valid(content_formset)

    def get_success_url(self):
        return reverse_lazy('accounts:item_detail',  kwargs={'pk': self.object.pk})



