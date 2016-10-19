"""sookhproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import JavaScriptCatalog




urlpatterns=[
    #url(r'^jsi18n/$', JavaScriptCatalog.as_view(packages=['appwithmodels']), name='javascript-catalog'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
   # url(r'^rosetta/', include('rosetta.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$',RedirectView.as_view(url='/sookh/home/',permanent=True)),
    url(r'^search/', include('haystack.urls')),
    url(r'^sookh/',include('appwithmodels.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

