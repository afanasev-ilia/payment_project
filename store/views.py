from typing import Any
import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView

from store.models import Item

YOUR_DOMAIN = "http://127.0.0.1:8000"

stripe.api_key = settings.STRIPE_SECRET_KEY


class ProductLandingPageViev(TemplateView):
    template_name = 'store/landing.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        product = Item.objects.get(name='Подписка ++')
        context = super(ProductLandingPageViev, self).get_context_data(**kwargs)
        context.update({
            "product": product,
            "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY
        })
        return context


class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': '{{PRICE_ID}}',
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        return JsonResponse({"id": checkout_session.id})
