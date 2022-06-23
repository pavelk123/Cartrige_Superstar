
from django.urls import path,include

from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'cartrige',views.CartrigeViewSet,) 
print(router.urls)
urlpatterns = [
    path('',views.api_home),#'http://127.0.0.1:8000/api/'
    #path('ca/',views.CartrigeViewSet.as_view({'get':'list'})),
    #path('create/printer_producer/',views.api_create_printer_producer),
    # path('catalog/cartridge/all',views.CartrigeAPIList.as_view()),
    # path('catalog/cartridge/<int:id>',views.CartrigeAPIView.as_view(),)
    path(r'catalog/', include(router.urls))
]
