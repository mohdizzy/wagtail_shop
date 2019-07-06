from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView


class IndexPage(TemplateView):
    template_name = 'index.html'

class HomePage(TemplateView):
    template_name = "home/home_page.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            print(request.user)
            return HttpResponseRedirect(reverse("index"))
        return super().get(request, *args, **kwargs)
