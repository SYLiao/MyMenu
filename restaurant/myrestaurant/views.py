from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.http import HttpResponseRedirect
from .models import Restaurant, Dish, RestaurantReview
from .forms import RestaurantForm

# Create your views here.

class ListRestaurant(ListView):

    context_object_name = 'restaurant_list'
    template_name = 'restaurant_list.html'

    def get_queryset(self):
        return Restaurant.objects.all().order_by('-date')

class RestaurantDetail(DetailView):

    model = Restaurant
    context_object_name = 'Details'
    template_name = 'DetailRestaurant.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['RATING_CHOICES'] = RestaurantReview.Ratingchoice
        return context

class RestaurantCreate(CreateView):

    model = Restaurant
    template_name = 'form.html'
    form_class = RestaurantForm

    def form_invalid(self, form):
        form.instance.user = self.request.user
        return super().form_invalid(form)

class RestaurantUpdate(UpdateView):

    model = Restaurant
    form_class = RestaurantForm
    template_name = 'form.html'