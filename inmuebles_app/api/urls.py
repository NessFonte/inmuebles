from django.urls import path, include
from rest_framework.routers import DefaultRouter
#from inmuebles_app.api.views import inmuebles_list, inmueble_id #Importacion de los servicios por métodos
from inmuebles_app.api.views import (EdificacionAV, EdificacionDetailAV, ComentarioList, ComentarioDetail, 
ComentarioCreate, EmpresaVS) #Importacion de los servicios por clases

router = DefaultRouter()
router.register('empresa', EmpresaVS, basename="empresa")

urlpatterns = [
    path('edificacion/', EdificacionAV.as_view(), name="edificacion-list"),
    path('edificacion/<int:pk>', EdificacionDetailAV.as_view(), name="edificacion-detail"),
    
    path('', include(router.urls)),
    #path('empresa/', EmpresaAV.as_view(), name="empresa-list"),
    #path('empresa/<int:pk>', EmpresaDetailAV.as_view(), name="empresa-detail"),
    
    path('edificacion/<int:pk>/comentario-create/', ComentarioCreate.as_view(), name="comentario-create"),
    path('edificacion/<int:pk>/comentario/', ComentarioList.as_view(), name="comentario-list"),
    path('edificacion/comentario/<int:pk>', ComentarioDetail.as_view(), name="comentario-detail"),
]