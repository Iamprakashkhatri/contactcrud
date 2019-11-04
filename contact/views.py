from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.core.urlresolvers import reverse_lazy
from .models import Contact

class ContactList(ListView):
    template_name = 'contact_list.html'
    model = Contact

class ContactDetail(DetailView):
    template_name = "contact_details.html"
    model = Contact

class ContactCreate(CreateView):
    template_name = "contact_form.html"
    model = Contact
    fields = ['name','email','address','phone']

class ContactUpdate(UpdateView):
    template_name = "contact_form.html"
    model = Contact
    fields = ['name', 'email', 'address', 'phone']
class ContactDelete(DeleteView):
    template_name = 'contact_confirm_delete.html'
    model = Contact
    # success_url = reverse('contact:contact_list')

    def get_success_url(self):
        return reverse('contact:contact_list')