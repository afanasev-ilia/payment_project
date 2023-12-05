from typing import Any

import stripe
from django.conf import settings
from django.db.models.query import QuerySet
from django.http import HttpRequest
from django.shortcuts import HttpResponse, redirect
from django.views import View
from django.views.generic import TemplateView

from store.models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY


class IndexPageView(TemplateView):
    template_name = 'store/index.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, QuerySet]:
        context = super().get_context_data(**kwargs)
        context['items'] = Item.objects.all()
        return context


class SuccessPageView(TemplateView):
    template_name = 'store/success.html'


class CancelPageView(TemplateView):
    template_name = 'store/cancel.html'


class ItemPageView(TemplateView):
    template_name = 'store/item.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        item = Item.objects.get(id=self.kwargs['id'])
        context = super().get_context_data(**kwargs)
        context.update(
            {
                'item': item,
                'STRIPE_PUBLIC_KEY': settings.STRIPE_PUBLIC_KEY,
            }
        )
        return context


class CreateCheckoutSessionView(View):
    def get(
        self, request: HttpRequest, *args: Any, **kwargs: Any
    ) -> HttpResponse:
        product = Item.objects.get(id=self.kwargs['id'])
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': product.price,
                        'product_data': {
                            'name': product.name,
                        },
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=settings.YOUR_DOMAIN + '/success/',
            cancel_url=settings.YOUR_DOMAIN + '/cancel/',
        )
        return redirect(checkout_session.url, code=303)
