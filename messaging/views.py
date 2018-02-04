from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Message
from .forms import MessageForm

def mailbox(request):
	messages = Message.objects.filter()
	return render(request, 'messaging/mailbox.html', { 'messages': messages })

def create_message(request):
	if request.method == 'POST':
		form = MessageForm(request.POST)
		if form.is_valid():
			message = form.save(commit = False)
			message.sender = request.user
			message.receiver = request.user # CHANGE THIS LATER
			message.save()
			# Events won't be stored, call them every time
			# when drawing templates
			return render(request, 'messaging/confirmation.html', { })
	else:
		form = MessageForm()
	return render(request, 'messaging/create_message.html', { 'form': form })

