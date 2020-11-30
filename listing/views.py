from django.shortcuts import render
from .models import Listing
from django.contrib.auth.models import User
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from .forms import ListingForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class ListingView(ListView):
    model = Listing
    template_name = 'listing/homepage.html'
    context_object_name = 'all_listings'


class ListingDetailView(DetailView):
    model = Listing
    template_name = 'listing/listing_details.html'

class AddListingView(LoginRequiredMixin,CreateView):
    model = Listing
    template_name = 'listing/listing_add.html'
    redirect_field_name = 'listing/listing_details.html'
    form_class = ListingForm

class DeleteListingView(LoginRequiredMixin,DeleteView):
    model = Listing
    template_name = 'listing/listing_delete.html'
    success_url = reverse_lazy('listing:all_listing')

class UpdateListingView(LoginRequiredMixin,UpdateView):
    model = Listing 
    redirect_field_name = 'listing/listing_details.html'
    template_name = 'listing/listing_add.html'
    form_class = ListingForm



