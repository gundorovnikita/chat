from django.shortcuts import render, redirect
from .models import *
from .forms import *
import random

# Create your views here.
def index(request):
	message = Message.objects.all()
	message_id = message[9].id + 1
	if request.method == 'POST':
		create = send_message(request.POST)
		if create.is_valid():
			create.save()
			return redirect('index_url')
	else:
		create = send_message()

	context = {
		'message':message,
		'create':create,
		'message_id':message_id,
	}
	return render(request, 'index.html', context)