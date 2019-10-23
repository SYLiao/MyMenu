from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class Restaurant(models.Model):

    name = models.TextField('Restaurant Name', max_length=50)
    address = models.TextField('Address', max_length=200, blank=True, default='')
    telephone = models.TextField('Telephone number', max_length=20, blank=True, default='')
    url = models.URLField('Offical Website', blank=True, default='')
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    date = models.DateTimeField('Create Time', default=timezone.now())

    objects = models.Manager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('myrestaurant : restaurant_detail', args={str(self.id)})

class Dish(models.Model):

    name = models.TextField('Dish name')
    description = models.TextField('Dish description', blank=True, default='')
    price = models.DecimalField('Dish price', max_digits=8, decimal_places=2, blank=True, null=True)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    date = models.DateTimeField('Create time', default=timezone.now())
    image = models.ImageField(upload_to='myrestaurant', blank=True, null=True)
    restaurant = models.ForeignKey(Restaurant, default=1, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('myrestaurant : dish_detail', args=[str(self.restaurant.id), str(self.id)])

class Review(models.Model):

    Ratingchoice = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
    Rating = models.SmallIntegerField('Rating (stars)', blank=False, default=5, choices=Ratingchoice)
    user = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    date = models.DateTimeField('Create time', default=timezone.now())
    comment = models.TextField('Comment', max_length=200, blank=True, null=True)

    class Meta:
        abstract = True

class RestaurantReview(Review):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return str(self.restaurant.name)
