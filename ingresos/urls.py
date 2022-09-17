from django.urls import path, include
from .views import *
urlpatterns = [

    path('accounts/', include('django.contrib.auth.urls')),
    path('historial/', BetList.as_view(), name='bet-index'),
    path('historial/crear/', BetCreate.as_view(), name='bet-create'),
    path('historial/<int:pk>/', BetUpdate.as_view(), name='bet-update'),
    path('historial/<int:pk>/eliminar/', BetDelete.as_view(), name='bet-delete'),
]
