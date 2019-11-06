from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

def validate_domainonly_email(value):
    if not "your@domain.com" in value:
        raise ValidationError(_("Sorry,the email submitted is invalid"))
    return value

Blacklisted=['abc','new']
def validate_blacklisted(value):
    if value in Blacklisted:
        raise ValidationError(_("Sorry,the value is not valid."))
    return value
