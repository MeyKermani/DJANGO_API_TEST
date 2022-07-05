from django.db import models
from django.db.models import Count
from django.contrib.auth.models import UserManager
import Users.models


class CustomUserManager(UserManager):
    def get_users_with_three_addresses(self, limited_address_count):
        Users.models.CustomUser.address_limit = limited_address_count
        return self.all().annotate(address_count=Count('addresses'))


class AddressManager(models.Manager):
    def help_desk_addresses(self):
        return self.filter(creator='HELPDESK')