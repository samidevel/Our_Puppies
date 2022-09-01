from django.contrib import admin
from .models import User, UserProfile
from .models import Socialpublication
from .models import Socialcomment

admin.site.register(Socialpublication)	
admin.site.register(Socialcomment)
admin.site.register(UserProfile)