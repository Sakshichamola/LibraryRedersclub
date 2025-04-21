from django import forms
from datetime import date
from .models import *

CATEGORY_CHOICES = [
    ('popular','Popular'),
    ('new_Arrivals','New_Arrivals'),
    ('business', 'Business'),
    ('newspaper', 'Newspaper'),
    ('magazine', 'Magazine'),
    ('lifestyles','Lifestyles'),
    ('entertainment','Entertainment'),
    ('sport','Sport'),
    ('fashion', 'Fashion'),
    ('technology', 'Technology'),
    ('comic', 'Comic'),
    ('autocar', 'Autocar'),                          
    ('health','Health'),
    ('holiday','Holiday'),
    ('competitive_exam','Competitive_Exam'),
    ('fitness','Fitness'),
]
class PublisherForm(forms.Form):
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, required=True)
    title = forms.CharField(max_length=255, required=True)
    image = forms.ImageField(required=True)
    date = forms.DateField(initial=date.today, widget=forms.DateInput(attrs={'type': 'date'}))
    rating = forms.DecimalField(max_digits=2, decimal_places=1, min_value=0, max_value=5, required=True)
    readers_count = forms.IntegerField(min_value=0, required=True)
