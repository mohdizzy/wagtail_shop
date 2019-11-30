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


urlpatterns = [
    url(r'^$', views.IndexPage.as_view(), name="index"),
    url(r'^home/', views.HomePage.as_view(), name="home"),
    url(r'^delete-cart/', mainView.deletecart, name='delete-cart'),
    url(r'^address-select/', mainView.AddressSelectionView.as_view(), name='address-select'),
    url(r'^selected-address/', mainView.SelectedAddress, name='selected-address'),
    url(r'^account-details/$', mainView.AccountDetailsView.as_view(), name="account-details"),
    url(r'^account-details/login_security/$', mainView.LoginSecurityView.as_view(), name="login-security"),
    url(r'^account-details/login_security/change_name/(?P<pk>\d+)/edit/', mainView.ChangeNameView.as_view(),
        name="change-name"),
    url(r'^account-details/orders/', mainView.OrderDetail.as_view(), name="order"),
    url(r'^account-details/address-manage/$', mainView.AddressManageView.as_view(), name='address-manage'),
    url(r'^account-details/login_security/change_number/(?P<pk>\d+)/edit/', mainView.ChangePhoneView.as_view(),
        name="change-number"),
    # url(r'^account-details/login_security/edit_name', mainView.ChangeNameView.as_view(), name="change-name"),

    url(r'^django-admin/', admin.site.urls),

    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),

    url(r'^search/$', search_views.search, name='search'),
    url(r'accounts/', include('allauth.urls')),



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
