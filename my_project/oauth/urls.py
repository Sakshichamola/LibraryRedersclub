from django.urls import path
from . import views
from oauth.views import custom_login
from oauth.views import signup_view
from oauth.views import logout_view

urlpatterns = [
   path('login/', custom_login, name='login'),
   path('signup/', signup_view, name='signup'),
   path('logout/', logout_view, name='logout'),
   path('profile/', views.profile, name='profile'),
   path('settings/', views.settings, name='settings'),
   path('purchase-history/', views.purchase_history, name='purchase_history'),
]




# from django.urls import path
# from django.contrib.auth.views import LoginView, LogoutView
# from . import views

# urlpatterns = [
#     path('login/', LoginView.as_view(template_name='login.html'), name='login'),
#     path('signup/', views.signup, name='signup'),
#     path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
# ]
