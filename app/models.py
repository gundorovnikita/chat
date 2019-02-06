from django.db import models

# Create your models here.
class Message(models.Model):
	content = models.CharField(max_length = 250)

#	def save(self):
#		model = Message.objects.all()
#		if model.count() == 4:
#			model[1].delete()
