from django.urls import path
from slotBooking.views import UserProfileListView, ParkingListView, ReversationSlotView, ReservationView

urlpatterns = [
	path('signup/', UserProfileListView.as_view(), name='user-details'),
	path('parkings/', ParkingListView.as_view(), name='all-parkings'),
	path('reversations/', ReversationSlotView.as_view(), name='all-reservations'),
	path('reversation/<int:user_id>/', ReservationView.as_view(), name='reservation')

]