from django.db import models
import uuid


class AbstractCommonInfo(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        abstract = True
