from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required	

app_name = "foro"



urlpatterns = [
	#Busqueda 127.0.0.1:8000/foro
    url(r'^$', login_required(views.index), name='index'),
	
	#Busqueda 127.0.0.1:8000/foro/register
	url(r'^register/$', views.register, name='register'),
	
	#Busqueda 127.0.0.1:8000/foro/log
	url(r'^log/$', views.login_user, name='login_user'),
	
	#Busqueda 127.0.0.1:8000/foro/log_out
	url(r'^log_out/$', views.logout_user, name='log_out'),

	#Posts de las sección de anuncios 127.0.0.1:8000/foro/anuncios
	url(r'^anuncios/$', views.anuncios, name='anuncios'),
	
	#Hilo 127.0.0.1:8000/foro/anuncios/hilo
	url(r'^anuncios/hilo/$', views.hilo, name='hilo'),

]
