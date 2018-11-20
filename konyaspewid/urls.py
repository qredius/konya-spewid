from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
admin.autodiscover()
from konyaspewid import views as konyaspewid_views

urlpatterns = [
    url(r'^$', konyaspewid_views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^aboutus$', konyaspewid_views.aboutus, name='aboutus'),
	url(r'^vacancies$', konyaspewid_views.vacancies, name='vacancies'),
	url(r'^contact$', konyaspewid_views.contact, name='contact'),
    url(r'^portfolio$', konyaspewid_views.portfolio, name='portfolio'),
    url(r'^services$', konyaspewid_views.services, name='services'),
    url(r'^aboutevr$', konyaspewid_views.aboutevr, name='aboutevr'),
    url(r'^abouthaw$', konyaspewid_views.abouthaw, name='abouthaw'),
    url(r'^abouthr$', konyaspewid_views.abouthr, name='abouthr'),
]
