from django.urls import path

from store import views
from store.apps import StoreConfig

app_name = StoreConfig.name

urlpatterns = [
    path(
        '',
        views.IndexPageView.as_view(),
        name='index',
    ),
    path(
        'item/<id>/',
        views.ItemPageView.as_view(),
        name='item-page',
    ),
    path(
        'buy/<id>/',
        views.CreateCheckoutSessionView.as_view(),
        name='create-checkout-session',
    ),
    path('cancel/', views.CancelPageView.as_view(), name='cancel'),
    path('success/', views.SuccessPageView.as_view(), name='success'),
]
