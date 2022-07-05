from django.contrib import admin
from Utils.admin import all_fields_admin
from Users.models import CustomUser, Address


admin.site.register(CustomUser, all_fields_admin(CustomUser))
admin.site.register(Address, all_fields_admin(Address))