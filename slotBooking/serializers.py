from rest_framework import serializers
from slotBooking.models import UserProfile, Parking, ReservationSlot
from django.utils.crypto import get_random_string

class UserProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserProfile
		fields = ['phone_number', 'email', 'password']
		extra_kwargs = {
			'password': {'write_only': True},
			'phone_number': {'required': False},
			'email': {'required': False},
		}

	def validate_phone_number(self, phone_number):
		if phone_number and UserProfile.objects.filter(
			phone_number=phone_number).exists():
			raise serializers.ValidationError("Phone number is already exists")
		return phone_number

	def validate_email(self, email):
		if email and UserProfile.objects.filter(
			email=email).exists():
			raise serializers.ValidationError("email is already exists")
		return email

	def validate(self, data):
		phone_number = data.get('phone_number')
		email = data.get('email')
		#to check there should be one of the field user give input for that
		if not phone_number and not email:
			raise serializers.ValidationError("Please enter either \
				phone number or email.")
		return data

	def create(self, data):
		automated_username = get_random_string(length=16)
		user_profile_object = UserProfile.objects.create_user(
			username = automated_username,
			phone_number = data.get('phone_number'),
			email = data.get('email'),
			password = data.get('password')
		)
		return user_profile_object


class ParkingSerializer(serializers.ModelSerializer):
	class Meta:
		model = Parking
		fields = '__all__'


class ReservationSlotSerializer(serializers.ModelSerializer):
	class Meta:
		model = ReservationSlot
		fields = ['hours', 'user_profile', 'parking', 'price']
		extra_kwargs = {
			'price': {'read_only': True, 'required': False},
		}