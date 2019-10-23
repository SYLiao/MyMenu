from django.forms import ModelForm, TextInput, URLInput
from .models import Restaurant, Dish

class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        exclude = ('user', 'date', )

        widgets = {
            'name': TextInput({'class': 'form-control'}),
            'address': TextInput({'class': 'form-control'}),
            'telephone': TextInput({'class': 'form-control'}),
            'url': URLInput({'class': 'form-control'}),
        }

        labels = {
            'name': "Restaurant Name",
            'address': "Address",
            "telephone": "Phone number",
            "url": "Website",
        }