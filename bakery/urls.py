from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from search import views as search_views

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from longclaw import urls as longclaw_urls
from home import views
from . import views as mainView
from django.urls import path

urlpatterns = [
    url(r'^$', views.IndexPage.as_view(), name="index"),
    url(r'^home/', views.HomePage.as_view(), name="home"),
    url(r'^orders/', mainView.OrderDetail.as_view(), name="order"),
    url(r'^account-details/', mainView.AccountDetails.as_view(), name="account-details"),

    url(r'^django-admin/', admin.site.urls),

    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),

    url(r'^search/$', search_views.search, name='search'),

    path('basket/delete-cart/', mainView.deletecart, name='delete-cart'),
    url(r'^address-select/$', mainView.AddressView.as_view(), name='address-select'),
    url(r'^final-checkout/$', mainView.FinalCheckoutView.as_view(), name='final-checkout'),

    url(r'', include(longclaw_urls)),
    url(r'', include(wagtail_urls))
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    import debug_toolbar

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += url(r'^__debug__/', include(debug_toolbar.urls)),
