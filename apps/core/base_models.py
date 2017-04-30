from django.contrib.gis.db import models


class BaseTimeCreateModifyModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modify = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
