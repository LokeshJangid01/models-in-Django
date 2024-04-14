# def run():
#     print('L0ki')

from core.models import Restaurant
from django.utils import timezone
from django.db import connection

def run():
    #METHOD 1
        # restaurant = Restaurant()
        # restaurant.name = 'My Italian Restaurant'
        # restaurant.latitude = 50.2
        # restaurant.longitude = 55.2
        # restaurant.date_opened = timezone.now()
        # restaurant.restaurant_type = restaurant.TypeChoices.ITALIAN

        # restaurant.save()
    #METHOD 2

    Restaurant.objects.create(
        name = 'Pizza Shop',
        date_opened = timezone.now(),
        restaurant_type = Restaurant.TypeChoices.ITALIAN,
        latitude = 45.3,
        longitude = 40.5,

    )
    # print(restaurant)
    print(connection.queries)
