from django.db import models
from django.utils.translation import gettext_lazy as _

STATE_LIST = (
    ('Balochistan', 'Balochistan'),
    ('Khyber Pakhtunkhwa', 'Khyber Pakhtunkhwa'),
    ('Punjab', 'Punjab'),
    ('Sindh', 'Sindh')
)

GENDER_CHOICE = [
    ('Male', 'Male'),
    ('Female', 'Female')
]

# Resume Model
class Resume(models.Model):

    id = models.AutoField(primary_key=True)
    full_name = models.CharField(_("Full Name"), max_length=50)
    father_name = models.CharField(_("Father Name"), max_length=50)
    dob = models.DateField(_("Date of Birth"), auto_now=False, auto_now_add=False)
    gender = models.CharField(_("Gender"), max_length=50, choices=GENDER_CHOICE)
    city = models.CharField(_("City"), max_length=50)
    pin = models.PositiveIntegerField(_("City Post code"))
    mobile = models.PositiveIntegerField(_("Mobile Number"))
    email = models.EmailField(_("Email Adress"), max_length=254)
    job_city = models.CharField(_("JOb city"), max_length=50)
    state = models.CharField(_("Select State"), max_length=50, choices=STATE_LIST)
    image = models.ImageField(_("Uploade Image"), upload_to='images')
    file = models.FileField(_("Resume PDF"), upload_to='document')