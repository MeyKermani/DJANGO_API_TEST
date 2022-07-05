from django.db import models
from django.contrib.auth.models import AbstractUser
from Utils.models import AbstractCommonInfo
from Users.managers import CustomUserManager, AddressManager
from Users.validators import validate_latitude, validate_longitude, validate_phone
from Users.choices import ADDRESS_CREATORS


class CustomUser(AbstractUser, AbstractCommonInfo):
    address_limit = 3
    phone = models.CharField(max_length=11, validators=[validate_phone])
    objects = CustomUserManager()

    @property
    def address_count(self):
        return Address.objects.filter(user=self).count()

    @property
    def last_addresses(self):
        return Address.objects.filter(user=self).order_by('-created')[:self.address_limit]

    def get_address_limit(self):
        return self.address_limit

    def set_address_limit(self, limit):
        self.address_limit = limit

    def __str__(self):
        return f"USER::{self.phone}"

    def __repr__(self):
        return self.__str__()


class Address(AbstractCommonInfo):
    user = models.ForeignKey(CustomUser, related_name="addresses", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    latitude = models.FloatField(validators=[validate_latitude])
    longitude = models.FloatField(validators=[validate_longitude])
    creator = models.CharField(max_length=20, choices=ADDRESS_CREATORS)
    objects = AddressManager()

    def __str__(self):
        return f"ADDRESS::{self.title}"

    def __repr__(self):
        return self.__str__()