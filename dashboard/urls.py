from django.urls import path
from .views import *

urlpatterns = [
    path('', Index, name='index'),
    # INFO
    path('info/', AddInfo, name='add-info'),
    path('list-info/', ListInfo, name='list-info'),
    path('edit-info/<int:pk>/', EditInfo, name='edit-info'),
    path('delete-info/<int:pk>/', DeleteInfo, name='delete-info'),
    # Social Media
    path('social-media/', AddSocialMedia, name='add-social-media'),
    path('list-social-media/', ListSocialMedia, name='list-social-media'),
    path('edit-social-media/<int:pk>/', EditSocialMedia, name='edit-social-media'),
    path('delete-social-media/<int:pk>/', DeleteSocialMedia, name='delete-social-media'),
    # Order
    path('list-order/', ListOrder, name='list-order'),
    path('edit-order/<int:pk>/', EditOrder, name='edit-order'),
    path('delete-order/<int:pk>/', DeleteOrder, name='delete-order'),
    # Product
    path('product/', AddProduct, name='add-product'),
    path('list-product/', ListProduct, name='list-product'),
    path('edit-product/<int:pk>/', EditProduct, name='edit-product'),
    path('delete-product/<int:pk>/', DeleteProduct, name='delete-product'),
    # About Product
    path('about-product/', AddAboutProduct, name='add-about-product'),
    path('list-about-product/', ListAboutProduct, name='list-about-product'),
    path('edit-about-product/<int:pk>/', EditAboutProduct, name='edit-about-product'),
    path('delete-about-product/<int:pk>/', DeleteAboutProduct, name='delete-about-product'),
    # About Company
    path('about-company/', AddAboutCompany, name='add-about-company'),
    path('list-about-company/', ListAboutCompany, name='list-about-company'),
    path('edit-about-company/<int:pk>/', EditAboutCompany, name='edit-about-company'),
    path('delete-about-company/<int:pk>/', DeleteAboutCompany, name='delete-about-company'),
    # Who Use
    path('whouse/', AddWhoUse, name='add-who-use'),
    path('list-whouse/', ListWhoUse, name='list-who-use'),
    path('edit-whouse/<int:pk>/', EditWhoUse, name='edit-who-use'),
    path('delete-whouse/<int:pk>/', DeleteWhoUse, name='delete-who-use'),
    # How To Use
    path('howtouse/', AddHowtoUse, name='add-how-to-use'),
    path('list-howtouse/', ListHowtoUse, name='list-how-to-use'),
    path('edit-howtouse/<int:pk>/', EditHowtoUse, name='edit-how-to-use'),
    path('delete-howtouse/<int:pk>/', DeleteHowtoUse, name='delete-how-to-use'),
    # Fact
    path('fact/', AddFact, name='add-fact'),
    path('list-fact/', ListFact, name='list-fact'),
    path('edit-fact/<int:pk>/', EditFact, name='edit-fact'),
    path('delete-fact/<int:pk>/', DeleteFact, name='delete-fact'),
]