from django.apps import AppConfig


class CheckoutConfig(AppConfig):
    name = 'checkout'

    def ready(self):
        """
        Overriding the ready method and importing our signals module
        will let Django know that there's a new signals module with
        some listeners in it.
        So now every time a line item is saved or deleted, our custom
        update total model method will be called, updating the order
        totals automatically.
        """
        import checkout.signals
