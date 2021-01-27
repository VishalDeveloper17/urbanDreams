from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Blocks)
admin.site.register(Flats)
admin.site.register(Maintenance)
admin.site.register(Services)