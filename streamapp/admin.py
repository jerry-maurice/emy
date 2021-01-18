from django.contrib import admin
from streamapp.models import Tweet, Item, Follow

# Register your models here.
admin.site.register(Tweet)
admin.site.register(Item)
admin.site.register(Follow)

