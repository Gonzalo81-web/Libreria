from django.urls import path, include
from .views import home , contacto , index, compra, registro, LibroViewset, error_facebook
from rest_framework import routers


#Permite crear las url necesarias para la aplicacion
#ademas genera url para listar eliminar
router = routers.DefaultRouter()
#No es necesario que la llamemos libros pero tiene que tener relacion como se van a pasar los datos a una determinada url
router.register('libro', LibroViewset)


urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('index/', index, name="index"),
    path('compra/', compra, name="compra"),
    path('registro/', registro, name="registro"),
    path('api/', include(router.urls)),
    path('error-facebook/', error_facebook, name="error_facebook"),
]
