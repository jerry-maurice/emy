from django.contrib import admin
from contest.models import Videolibrary, Like, Rating

# Register your models here.
admin.site.register(Videolibrary)
admin.site.register(Like)
admin.site.register(Rating)