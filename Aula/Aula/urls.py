from django.conf.urls import url

from . import views
from Aula.views import leo


urlpatterns = [
	url(r'^leo/$', leo),
	url(r'^$', leo),
	
]
