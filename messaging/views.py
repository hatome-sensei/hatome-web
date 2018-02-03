from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import MessageForm

def mailbox(request):
	return render(request, 'messaging/mailbox.html', {})

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

