from django.contrib import admin
from readng.profiles.models import UserProfile, ConnectedAccount

admin.site.register(UserProfile)
admin.site.register(ConnectedAccount)
