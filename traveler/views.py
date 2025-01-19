from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, TemplateView
from django.urls import reverse_lazy, reverse
from .forms import TravelerForm
from .models import Traveler

# Usermodel = get_user_model

class TravelerCreateView(CreateView):
    model = Traveler
    form_class = TravelerForm
    template_name = 'create-traveler.html'
    success_url = reverse_lazy('all-trips')  # Redirect to All Trips after creation
    # success_url = reverse_lazy('details-traveler')  # Redirect to All Trips after creation

    def form_valid(self, form):
        # You can add any additional processing here before saving
        return super().form_valid(form)

    # def get_success_url(self):
    #     # Redirect to the newly created traveler's detail page
    #     return reverse('details-traveler', kwargs={'pk': self.object.pk})

    # def dispatch(self, *args, **kwargs):
    #     # Custom logic (if needed)
    #     if self.request.user.is_authenticated:
    #         logout(self.request)
    #     return super().dispatch(*args, **kwargs)
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = 'Create New Traveler'
    #     return context
    #
    # def form_valid(self, form):
    #     # Save the Traveler instance
    #     traveler = form.save()
    #
    #     # Retrieve or create the associated User
    #     user, created = User.objects.get_or_create(username=traveler.nickname)
    #     if created or user.email != traveler.email:
    #         user.email = traveler.email
    #         user.save()
    #
    #     # Log the user in
    #     login(self.request, user)
    #
    #     return super().form_valid(form)


# def TravelerDetailsView(request):
#     # traveler = get_traveler()
#     traveler = get_object_or_404(Traveler)
#
#     context = {
#         'traveler': traveler,
#     }
#
#     return render(request, template_name='details-traveler.html', context=context)


class TravelerDetailView(DetailView):
    model = Traveler
    template_name = 'details-traveler.html'
    context_object_name = 'traveler'
    # traveler = get_object_or_404(Traveler)

    # def get_object(self):
    #     return get_object_or_404(Traveler, id=self.kwargs.get('id'))
    # get_object = get_object_or_404(Traveler, pk=['pk'])
    # get_object = get_object_or_404(Traveler, id=['id'])
    # get_object = get_object_or_404(Traveler)
    # def get_object(self, queryset=None):
    #     return get_object_or_404(Traveler)

    get_object = lambda self, queryset=None: get_object_or_404(Traveler)
    # def get_object(self):
    #     # Fetch the Chef based on the provided ID
    #     traveler_id = self.kwargs.get('id')
    #     return get_object_or_404(Traveler, id=traveler_id)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['traveler'] = Traveler.objects.all()  # Ensure this includes the pk
    #     return context


class TravelerUpdateView(UpdateView):
    model = Traveler
    form_class = TravelerForm
    template_name = 'edit-traveler.html'
    success_url = reverse_lazy('all-trips')  # Redirect to Traveler Details after edit

    def get_object(self):
        return get_object_or_404(Traveler)


class TravelerDeleteView(DeleteView):
    model = Traveler
    template_name = 'delete-traveler.html'
    success_url = reverse_lazy('index')  # Redirect to Index after deletion

    def get_object(self):
        return get_object_or_404(Traveler)


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Example: Add traveler existence flag for dynamic navigation
        # context['has_traveler'] = Traveler.objects.exists()
        context['traveler'] = Traveler.objects.all()
        return context

