from django.views import generic
from longclaw.orders.models import OrderItem

from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.contrib.auth import get_user_model
User = get_user_model()
from longclaw.basket.utils import destroy_basket, remove_from_basket
from longclaw.shipping.models import UserAddress
try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse

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

        return context

def deletecart(request):
   if request.POST['empty'] == 'Y':
       destroy_basket(request)
       return HttpResponse(200)
   remove_from_basket(request)
   return HttpResponse(200)


class AccountDetails(generic.TemplateView):
    template_name = 'account_details/account_details.html'


class AddressSelectionView(generic.TemplateView):
    template_name = "address/address_selection.html"

    def get_context_data(self, **kwargs):
        context = super(AddressSelectionView, self).get_context_data(**kwargs)

        context['stored_address'] = UserAddress.objects.filter(email=str(self.request.user)).distinct()

        return context


class FinalCheckoutView(generic.TemplateView):
    template_name = "checkout/final_checkout.html"

    # Receive selected address and it's ID to session token
    def post(self, request, *args, **kwargs):
        stored_address_id = request.POST['form-address-select']
        request.session['stored_address_id'] = stored_address_id

        return HttpResponseRedirect(reverse(
                'longclaw_checkout_view'))


class AddressManageView(generic.TemplateView):
    template_name = "address/address_management.html"

    def get_context_data(self, **kwargs):
        context = super(AddressManageView, self).get_context_data(**kwargs)

        context['stored_address'] = UserAddress.objects.filter(email=str(self.request.user)).distinct()

        return context

    def post(self, request, *args, **kwargs):

        UserAddress.objects.filter(id=request.POST['delete_address_id']).delete()
        print("deleted")

        return HttpResponseRedirect(reverse(
            'address-manage'))






