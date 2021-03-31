from django.http import HttpResponse


class StripeWH_Handler:
    """
    Handle Stripe webhooks:
    the idea being here is that for each type of webhook
    we would like a different method to handle it - which makes
    them easier to manage.
    """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
