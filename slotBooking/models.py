from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

#making this to not write added,updated datetime everytime while create new model
class DateData(models.Model):
	added_datetime = models.DateTimeField(auto_now_add=True)
	updated_datetime = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True

class UserProfile(AbstractUser):
	phone_number = models.CharField(max_length=15, blank=True, null=True, 
		default=None)

class Parking(DateData):
	address = models.TextField()
	longitude = models.FloatField()
	latitude = models.FloatField()

class ReservationSlot(models.Model):
	user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	parking = models.ForeignKey(Parking, on_delete=models.CASCADE)
	hours = models.PositiveIntegerField()
	price = models.DecimalField(max_digits=10, decimal_places=2)

	def calculate_partking_hours_price(self):
		self.price = self.hours * settings.RATE_PER_HOUR

	def save(self, *args, **kwargs):
		self.calculate_partking_hours_price()
		super().save(*args, **kwargs)