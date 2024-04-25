from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
from django.db.models.functions import Lower
# Create your models here.

def validate_res_name_start_with_a(value):
    if not value.startswith('a'):
        raise ValidationError('Res name does not start with a')
    
class Restaurant(models.Model):
    class TypeChoices(models.TextChoices):
        INDIAN = 'IN', 'Indian'
        CHINESE = 'CH', 'Chinese'
        ITALIAN = 'IT', 'Italian'
        GREEK = 'GR', 'Greek'
        MEXICAN = 'MX', 'Mexican'
        FASTFOOD = 'FF', 'Fast Food'
        OTHER = 'OT', 'Other'

    name = models.CharField(max_length = 100, validators = [validate_res_name_start_with_a])
    website = models.URLField(default = '')
    date_opened = models.DateField()
    latitude = models.FloatField(validators = [MinValueValidator(-90),MaxValueValidator(90)])
    longitude = models.FloatField(validators = [MinValueValidator(-180),MaxValueValidator(180)])
    restaurant_type = models.CharField(max_length = 2, choices = TypeChoices.choices)

    class Meta:
        ordering = [Lower('name')]

    def __str__(self):
        return f'{self.name} is opened on {self.date_opened}'
    
class Rating(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    restaurant = models.ForeignKey(Restaurant,on_delete = models.CASCADE,related_name = 'rating')
    rating = models.PositiveSmallIntegerField(
        validators = [MinValueValidator(1),MaxValueValidator(5)]
    )

    def __str__(self):
        return f"Rating of {self.restaurant} is {self.rating}"


class Sale(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete = models.SET_NULL, null = True, related_name = 'sales')
    income = models.DecimalField(max_digits = 5, decimal_places = 2)
    datetime = models.DateTimeField()

    def __str__(self):
        return f"Income of  {self.restaurant} is {self.income}"
    