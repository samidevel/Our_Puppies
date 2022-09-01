from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
#from django.db.models.signals import pre_save

# Create your models here.
"""class User(AbstractUser):
	perzonalized_user_id = models.CharField(max_length=60)"""



#initial creation the user profile

class UserProfile(models.Model):
	user    =   models.OneToOneField(User, on_delete=models.CASCADE)
	name    =   models.CharField(max_length=100, verbose_name ='Nombre')
	surname =   models.CharField(max_length=100, verbose_name = 'Apellido')
	email   =   models.EmailField(max_length=254)
	phone   =   models.IntegerField()
	image   =   models.ImageField(default='default.png')
	creation_date = models.DateField(auto_now_add=True)
	birthday      = models.DateField(null=True, blank=True)

	"""def create_user_profile_signals(sender, instance, created, **kwargs):
		if created:
			userprofile.objects.create(user=instance)

	def save_user_profile_signals(sender, instance, created, **kwargs):
		instance.userprofile.save()

	post_save.connect(create_user_profile_signals, sender=User)"""


#initial creation the user posts 
class Socialpublication(models.Model):
	timestamp = models.DateTimeField(default=timezone.now)
	content   = models.TextField()
	user      = models.ForeignKey(User, on_delete=models.CASCADE, related_name='publications')
	author    = models.ForeignKey(User, on_delete=models.CASCADE, related_name='social_publication_author')
	
	class Meta:
		ordering = ['-timestamp']

	def __str__(self):
		return self.content


#initial creation comment options
class Socialcomment(models.Model):
	publication     = models.ForeignKey(Socialpublication, on_delete=models.CASCADE)
	content_comment = models.TextField()
	create_date     = models.DateTimeField(default=timezone.now)
	author          = models.ForeignKey(User, on_delete=models.CASCADE, related_name='social_publication_comment')





