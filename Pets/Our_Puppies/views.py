from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Socialpublication, UserProfile, Socialcomment

# Create your views here.


def userpublication(request):
	socialpublication = Socialpublication.objects.all()
	#context = {'socialpublications':socialpublication}
	context ={'socialpublications':socialpublication}
	return render(request, "ourpuppies/userpublications.html", context)	