from django.shortcuts import render
from .models import Rating,Restaurant,Sale
from .form import RatingForm


# Create your views here.
def home(request):
    # restaurants = Restaurant.objects.all()
    restaurants = Restaurant.objects.prefetch_related('rating','sales')

    ratings = Rating.objects.select_related('restaurant')

    sales = Sale.objects.select_related('restaurant')


        
    context = {'restaurants':restaurants,
               'rating':ratings,
               'sales':sales
               
               }

    return render(request,'index.html',context=context)
