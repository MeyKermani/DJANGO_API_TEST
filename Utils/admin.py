from django.contrib import admin
from django.db.models import ManyToOneRel, ForeignKey, OneToOneField


def all_fields_admin(model):
    return type('SubClass'+model.__name__, (admin.ModelAdmin,), {
        'list_display': [x.name for x in model._meta.fields if x.name != "password"],
        'search_fields': [x.name for x in model._meta.fields],
        'list_filter': [x.name for x in model._meta.fields],
        'list_select_related': [x.name for x in model._meta.fields if isinstance(x, (ManyToOneRel, ForeignKey, OneToOneField,))]
    })

