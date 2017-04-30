from django.contrib.gis import admin

# Register your models here.
from apps.marker.models import Marker, Comment

admin.site.register(Marker, admin.GeoModelAdmin)
admin.site.register(Comment)