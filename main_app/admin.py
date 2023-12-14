from django.contrib import admin

from .models import Knot, TypeOfKnot

# Register your models here.
admin.site.register(Knot)
admin.site.register(TypeOfKnot)