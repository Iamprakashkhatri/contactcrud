from django.db import models
from django.urls import reverse
# from . validations import validate_domainonly_email,validate_blacklisted

class  Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)

    def get_absolute_url_detail(self):
        return reverse("contact:contact_detail",kwargs={"pk":self.pk})
    def get_absolute_url_update(self):
        return reverse("contact:contact_update",kwargs={"pk":self.pk})
    def get_absolute_url_delete(self):
        return reverse("contact:contact_delete",kwargs={"pk":self.pk})
    def __str__(self):
        return self.name