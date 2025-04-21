from django.urls import path
from .views import publisher_dashboard
from .views import user_dashboard, view_all, item_detail


urlpatterns = [
    path('', user_dashboard, name='user_dashboard'),
    path('publisher/', publisher_dashboard, name='publisher_dashboard'),
    path('viewall/', view_all, name='view_all'),
    path('item/<str:category>/<int:item_id>/', item_detail, name='item_detail'),
]





