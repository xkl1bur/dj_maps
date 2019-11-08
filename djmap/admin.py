from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from djmap.models import MushroomSpot

admin.site.register(MushroomSpot, LeafletGeoAdmin)
