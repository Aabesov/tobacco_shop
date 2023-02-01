from django.contrib import admin
from django.contrib.auth import get_user_model

from authentication.models import User, Favorite


admin.site.register(User)
admin.site.register(Favorite)
