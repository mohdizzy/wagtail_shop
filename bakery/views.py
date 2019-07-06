from django.views import generic
from longclaw.orders.models import OrderItem

from django.http import Http404
from django.contrib.auth import get_user_model
User = get_user_model()


class OrderDetail(generic.ListView):
    model = OrderItem
    template_name = "orders/order_detail.html"

    def get_queryset(self):
        try:
            self.orders_user = OrderItem.objects.filter(order__email=self.request.user.email).select_related('order')
        except User.DoesNotExist:
            raise Http404
        else:
            return self.orders_user.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["orders_user"] = self.orders_user
        print(context['orders_user'].values())
        return context



