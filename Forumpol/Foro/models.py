from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Post(models.Model):
	#RESPUESTA HACIA QUE POST (VACIO SI ES POST ORIGINAL
	reply_to = models.ForeignKey('self',blank=True, null=True,on_delete=models.SET_NULL)
	#Puede ser anuncio, Anuncio de CLUB , Vida Estudiantil
	content = models.CharField(max_length=300, default='')
	image = models.ImageField(upload_to='posted_images', blank=True)
	owner = models.ForeignKey(User,null=True,on_delete=models.SET_NULL)
	date = models.DateTimeField(auto_now=True)



class Thread(models.Model):
	#Original Post
	op = models.ForeignKey(Post,on_delete=models.CASCADE)
	#Puede ser anuncio, Anuncio de CLUB , Vida Estudiantil
	category = models.CharField(max_length=25, default='')
	topic = models.CharField(max_length=50, default='')
	
	