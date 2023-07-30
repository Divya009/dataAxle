from django.shortcuts import render
from rest_framework import generics
from slotBooking.models import UserProfile, Parking, ReservationSlot
from slotBooking.serializers import UserProfileSerializer, ParkingSerializer, ReservationSlotSerializer
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import GeometryDistance


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


class ParkingSlotListView(generics.ListAPIView):
	serializer_class = ParkingSerializer

	def get_queryset(self):
		lat = self.request.query_params.get('lat', None)
		lon = self.request.query_params.get('long', None)
		radius = self.request.query_params.get('radius', None)

		if not lat or not lon or not radius:
			return Parking.objects.none()

		location_object = Point(float(lon), float(lat), srid=4326)
		#for this we need to use PointField to pass the point object
		queryset = Parking.objects.annotate(
			location=GeometryDistance('address', location_object)
			).filter(location__lte=radius).order_by('location')
		return queryset