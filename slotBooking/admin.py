from django.contrib import admin
from slotBooking.models import *

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
	search_fields = ("phone_number","email")
	list_display = ['username','email','phone_number','first_name','last_name']


@admin.register(Parking)
class ParkingAdmin(admin.ModelAdmin):
	search_fields = ("latitude","longitude")
	list_display = [field.name for field in Parking._meta.get_fields()]

@admin.register(ReservationSlot)
class ReservationSlotAdmin(admin.ModelAdmin):
	list_display = [field.name for field in ReservationSlot._meta.get_fields()]