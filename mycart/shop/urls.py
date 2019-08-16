from django.urls import path
from . import views
from .models import Product
urlpatterns = [
   path("",views.index,name= 'ShopHome'),
   path("about/",views.aboutus,name= 'aboutus'),
   path('contact/',views.contact,name = "Contactus"),
   path("tracker/",views.tracker,name = 'Tracking status'),
   path('search/',views.search,name = "Search"),
   path('products/<int:my_id>',views.productview,name = 'productview'),
   path('checkout/',views.checkout,name= 'Checkout')
]
