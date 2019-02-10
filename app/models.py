from django.db import models

# Create your models here.
def validate(obj):
	message = Message.objects.all()
	if message.count() > 9:
		message[0].delete()

class Message(models.Model):
	content = models.CharField(max_length = 250)

	def clean(self):
		validate(self)

	def __str__(self):
		return self.content

