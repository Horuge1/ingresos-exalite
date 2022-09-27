from django.urls import path, include
from django.contrib.auth import views
from .views import *
urlpatterns = [

    path('accounts/login/', views.LoginView.as_view(authentication_form=UserLoginForm), name='login'),
    path('accounts/logout/', views.LogoutView.as_view(), name='logout'),
    path('', BetList.as_view()),
    path('historial/', BetList.as_view(), name='bet-index'),
    path('historial/crear/', BetCreate.as_view(), name='bet-create'),
    path('historial/<int:pk>/', BetUpdate.as_view(), name='bet-update'),
    path('historial/<int:pk>/eliminar/', BetDelete.as_view(), name='bet-delete'),
    path('herramientas/apuesta/', BetCalculator.as_view(), name='bet-calc'),
]
