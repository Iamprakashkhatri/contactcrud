from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
# from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render,redirect,get_object_or_404
from .models import Contact
from .forms import ContactForm

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

    success_url = reverse_lazy('contact:contact_list')

class ContactUpdate(UpdateView):
    template_name = "contact_form.html"
    model = Contact
    fields = ['name', 'email', 'address', 'phone']
    # def get_object(self):
    #     id_=self.kwargs.get("pk")
    #     return get_object_or_404(Contact, id=id_)

    success_url = reverse_lazy('contact:contact_list')

class ContactDelete(DeleteView):
    template_name = "contact_confirm_delete.html"

    model = Contact


    success_url = reverse_lazy('contact:contact_list')

    # def get_success_url(self):
    #     return reverse('contact:contact_list')
    # def delete(self, request, *args, **kwargs):
    #     """
    #     Call the delete() method on the fetched object and then redirect to the
    #     success URL.
    #     """
    #     self.object = self.get_object()
    #     success_url = reverse_lazy('contact:contact_list')
    #     self.object.delete()
    #     return HttpResponseRedirect(success_url)


def cont(request):
    if request.method=='POST':
        form=ContactForm(request.POST)
        if form.is_valid():
            try:
                # form.save()
                return redirect('')
            except:
                pass
    else:
        form = ContactForm()
    return render(request,"formvalidation.html",{'form':form})
