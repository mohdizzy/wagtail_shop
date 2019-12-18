from django.views import generic
from longclaw.configuration.models import Configuration
from longclaw.orders.models import OrderItem

from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.contrib.auth import get_user_model

from bakery.forms import ProfileForm, NameForm
from bakery.models import Profile
from django.shortcuts import get_object_or_404

User = get_user_model()
from longclaw.basket.utils import destroy_basket, remove_from_basket
from longclaw.shipping.models import UserAddress
try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .utils import render_to_pdf





class OrderDetail(LoginRequiredMixin,generic.ListView):
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


class AccountDetailsView(LoginRequiredMixin,generic.TemplateView):
    template_name = 'account_details/account_details.html'

class LoginSecurityView(LoginRequiredMixin,generic.TemplateView):
    template_name = 'account_details/login_security.html'


class ChangeNameView(LoginRequiredMixin,generic.UpdateView):
    model = User
    form_class = NameForm
    template_name = 'account_details/change_name.html'

    def get_object(self, *args, **kwargs):
        user = get_object_or_404(User, pk=self.kwargs['pk'])
        return user

    def get_success_url(self, *args, **kwargs):
        return reverse("account-details")

class ChangePhoneView(LoginRequiredMixin,generic.UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = "account_details/change_phone.html"

    def get_object(self, *args,**kwargs):
        user = get_object_or_404(User, pk=self.kwargs['pk'])
        return None

    def get_success_url(self, *args, **kwargs):
        return reverse("account-details")


class AddressSelectionView(LoginRequiredMixin,generic.TemplateView):
    template_name = "address/address_selection.html"

    def get_context_data(self, **kwargs):
        context = super(AddressSelectionView, self).get_context_data(**kwargs)

        context['stored_address'] = UserAddress.objects.filter(email=str(self.request.user.email)).distinct()

        return context


def SelectedAddress(request):

    # Receive selected address and it's ID to session token
    stored_address_id = request.POST['form-address-select']
    request.session['stored_address_id'] = stored_address_id

    return HttpResponseRedirect(reverse(
        'longclaw_checkout_view'))


class AddressManageView(LoginRequiredMixin,generic.TemplateView):
    template_name = "address/address_management.html"

    def get_context_data(self, **kwargs):
        context = super(AddressManageView, self).get_context_data(**kwargs)

        context['stored_address'] = UserAddress.objects.filter(email=str(self.request.user.email)).distinct()

        return context

    def post(self, request, *args, **kwargs):

        UserAddress.objects.filter(id=request.POST['delete_address_id']).delete()
        print("deleted")

        return HttpResponseRedirect(reverse(
            'address-manage'))


class GeneratePdf(generic.View):

    def get(self, request, *args, **kwargs):
        order_info = OrderItem.objects.filter(order__order_id=str(self.kwargs['pk'])).select_related('order')
        print(order_info)
        invoice_prefix = Configuration.for_site(request.site).invoice_prefix
        inv_data = {
             'invoice': order_info,
            'invoice_prefix':invoice_prefix,
        }
        pdf = render_to_pdf('invoice/invoice.html', inv_data)

        return HttpResponse(pdf, content_type='application/pdf')








