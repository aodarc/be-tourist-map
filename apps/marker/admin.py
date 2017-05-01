from django.contrib.gis import admin

# Register your models here.
from apps.marker.models import (
    Comment,
    Marker,
    Photo
)

admin.site.register(Marker, admin.GeoModelAdmin)
admin.site.register(Comment)
admin.site.register(Photo)
