from django.urls import path
from .views import ListRestaurant, RestaurantCreate, RestaurantDetail, RestaurantUpdate

app_name = 'myrestaurant'

urlpatterns = [
    path('', ListRestaurant.as_view(), name='list_restaurant'),
    path('create/', RestaurantCreate.as_view(), name='create_restaurant'),
    path('details/?P<pk>\d+', RestaurantDetail.as_view(), name='detail_restaurant'),
    path('update/?P<pk>\d+', RestaurantUpdate.as_view(), name='update_restaurant'),
]