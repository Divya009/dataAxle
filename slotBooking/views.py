from django.shortcuts import render
from rest_framework import generics
from slotBooking.models import UserProfile, Parking, ReservationSlot
from slotBooking.serializers import UserProfileSerializer, ParkingSerializer, ReservationSlotSerializer
from django.contrib.gis.geos import Point

class UserProfileListView(generics.ListCreateAPIView):
	queryset = UserProfile.objects.all()
	serializer_class = UserProfileSerializer


class ParkingListView(generics.ListAPIView):
	queryset = Parking.objects.all()
	serializer_class = ParkingSerializer


class ReversationSlotView(generics.ListCreateAPIView):
	queryset = ReservationSlot.objects.all()
	serializer_class = ReservationSlotSerializer


class ReservationView(generics.ListAPIView):
	serializer_class = ReservationSlotSerializer
	
	def get_queryset(self):
		user_id = self.kwargs['user_id']
		return ReservationSlot.objects.filter(user_profile_id=user_id)