from core.models import Restaurant, Rating, Sale
from django.utils import timezone
from django.db import connection
from django.contrib.auth.models import User
from pprint import pprint


def run():

    ##################          UPDATE          ####################3
    # restaurant = Restaurant.objects.filter(name__startswith = 'N')
    # pprint(restaurant)
    # # restaurant.name = 'New Restauant name'
    # # restaurant.save(update_fields=['name'])

    # restaurant.update(date_opened = timezone.now()-timezone.timedelta(days=500,weeks=50),website = 'https://www.dvnkdj.com')


    ###############         DELETE              ######################
    restaurant = Restaurant.objects.first()
    #Restaurant.objects.all().delete()
    pprint(restaurant.pk)
    pprint(restaurant.rating.all())
    pprint(restaurant.delete())
    pprint(connection.queries)
