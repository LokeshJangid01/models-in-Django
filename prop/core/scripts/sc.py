

from core.models import Restaurant, Rating, Sale
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User
from pprint import pprint

# def run():
#     #METHOD 1
#         # restaurant = Restaurant()
#         # restaurant.name = 'My Italian Restaurant'
#         # restaurant.latitude = 50.2
#         # restaurant.longitude = 55.2
#         # restaurant.date_opened = timezone.now()
#         # restaurant.restaurant_type = restaurant.TypeChoices.ITALIAN

#         # restaurant.save()
#     #METHOD 2

#     # Restaurant.objects.create(
#     #     name = 'Pizza Shop',
#     #     date_opened = timezone.now(),
#     #     restaurant_type = Restaurant.TypeChoices.ITALIAN,
#     #     latitude = 45.3,
#     #     longitude = 40.5,

#     # )
#     # print(restaurant)

#     #FOreign Key one to many relation
#         # restaurant = Restaurant.objects.first()
#         # user = User.objects.first()

#         # Rating.objects.create(user = user, restaurant = restaurant, rating = 3)

#     #FILTRING THE RECORDS
#     print(Rating.objects.filter(rating__gt = 3))
#     # Rating.objects.filter(rating = 5)



#     print(connection.queries)

###################                       UPDATING RECORD          ###################
def run():
    # restaurant = Restaurant.objects.first()
    # print(restaurant.name)

    # restaurant.name = 'Iatalian mama miya'
    # restaurant.save()

    #            REVERSE  RELATION

    #From restaurant get all rating

    # restaurant = Restaurant.objects.first()
    # print(restaurant.rating.all())


    # ##############        SALES   #############
    # Sale.objects.create(
    #     restaurant = Restaurant.objects.first(),
    #     income = 2.34,
    #     datetime = timezone.now()

    # )
    # Sale.objects.create(
    #     restaurant = Restaurant.objects.first(),
    #     income = 5.68,
    #     datetime = timezone.now()

    # )
    # Sale.objects.create(
    #     restaurant = Restaurant.objects.first(),
    #     income = 8.26,
    #     datetime = timezone.now()

    # )
    restaurant = Restaurant.objects.first()

    print(restaurant.sales.all())
    pprint(connection.queries)


