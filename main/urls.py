from django.urls import path
from .views import *


urlpatterns = [
    path('get-info-social/',get_info_social),
    path('create-order/',create_order),
    path('get-product/',get_product),
    path('get-about-product/',get_about_product),
    path('get-unity-product/',get_unity_product),
    path('get-about-company/',get_about_company),
    path('get-who-use/',get_who_use),
    path('get-how-to-use/',get_how_to_use),
    path('get-fact/',get_fact)
]