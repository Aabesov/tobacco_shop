from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from authentication.models import User
from tabaco_shop import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/accounts/', include("authentication.urls")),
    path('api/v1/products/', include("product.urls")),
    path('api/v1/orders/', include("order.urls")),
]
