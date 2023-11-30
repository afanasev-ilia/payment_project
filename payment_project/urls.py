from django.contrib import admin
from django.urls import include, path

from store.apps import StoreConfig

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls', namespace=StoreConfig.name)),
]
