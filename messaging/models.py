from random import choice, randint
from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.contrib.auth.models import User

WORKER_TYPES = (
	('BASIC', 'Mail pigeon'),
	('HARDY', 'Guerrilla pigeon'),
	('EMU',   'Ausie pigeon'),
	('SUSHI', 'Sushi pigeon'),
)

MAX_SEED_VALUE = 2147483647

def generate_seed():
	return randint(0, MAX_SEED_VALUE)

def random_worker_type():
	return choice(WORKER_TYPES)

class Message(models.Model):
	sender = models.ForeignKey(User,
		help_text = 'User who sent the message',
		related_name = 'senders',
		on_delete = models.CASCADE)
	receiver = models.ForeignKey(User,
		help_text = 'User who should receive the message',
		related_name = 'receivers',
		on_delete = models.CASCADE)
	content = models.TextField(
		help_text = 'Please keep the message interesting <3',
		validators = [
			MinLengthValidator(
				200,
				message = 'Messages need at least 200 chars'),
			MaxLengthValidator(
				400,
				message = 'Messages need to be under 400 chars')])
	worker = models.CharField(
		help_text = 'Kind of pigeon worker that will deliver message',
		max_length = 5,
		choices = WORKER_TYPES,
		default = random_worker_type)
	sent_date = models.DateTimeField(
		help_text = 'When the message was sent',
		auto_now = True)
	seed = models.PositiveIntegerField(
		help_text = 'Seed to use when generating events',
		default = generate_seed)
	events_seen = models.PositiveIntegerField(
		help_text = 'Amount of events that sender has seen',
		default = 0,
		editable = False)

	def __str__(self):
		return "Message<{}, {}, {}, {}, {}>".format(
			self.sender, self.receiver, self.worker,
			self.sent_date, self.seed)

