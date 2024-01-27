from django.urls import path
from django.urls import include

from lists import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('lists/', include('lists.urls'))
]
