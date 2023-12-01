from django.urls import path

from store import views
from store.apps import StoreConfig

app_name = StoreConfig.name

urlpatterns = [
    path(
        '',
        views.ProductLandingPageViev.as_view(),
        name='landing-page',
    ),
    path(
        'create-checkout-session/<pk>/',
        views.CreateCheckoutSessionView.as_view(),
        name='create-checkout-session',
    ),
]
