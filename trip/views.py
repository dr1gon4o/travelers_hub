from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

from .forms import TripForm
from .models import Trip

class TripListView(ListView):
    model = Trip
    template_name = 'all-trips.html'
    context_object_name = 'trips'
    ordering = ['-start_date']

class TripCreateView(CreateView):
    model = Trip
    form_class = TripForm
    template_name = 'create-trip.html'
    success_url = reverse_lazy('all-trips')
    # context_object_name = 'traveler'

    def form_valid(self, form):
        # Associate trip with the current traveler
        # form.instance.traveler = self.request.user.traveler
        return super().form_valid(form)

    # def form_valid(self, form):
    #     if not hasattr(self.request.user, 'traveler'):
    #         form.add_error(None, "You must create a traveler profile first!")
    #         return self.form_invalid(form)
    #     form.instance.traveler = self.request.user.traveler
    #     return super().form_valid(form)

class TripDetailView(DetailView):
    model = Trip
    template_name = 'details-trip.html'

class TripUpdateView(UpdateView):
    model = Trip
    form_class = TripForm
    template_name = 'edit-trip.html'
    success_url = reverse_lazy('all-trips')

class TripDeleteView(DeleteView):
    model = Trip
    template_name = 'delete-trip.html'
    success_url = reverse_lazy('all-trips')
