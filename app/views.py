from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.
def index(request):
	message = Message.objects.all()
	if request.method == 'POST':
		create = send_message(request.POST)
		if create.is_valid():
			create.save()
			return redirect('index_url')
	else:
		create = send_message()

	if message.count() == 10:
			message[0].delete()
	context = {
		'message':message,
		'create':create,
	}
	return render(request, 'index.html', context)