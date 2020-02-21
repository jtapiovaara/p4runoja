from django.urls import path
from . import views

urlpatterns = [
    path('', views.runoLista, name='runoLista'),
    path('uusi/', views.runoUusi, name='runoUusi')
    # path('korjaa/<int:runo_id>', views.runoKorjaa),
    # path('poista/<int:runo_id>', views.runoPoista)
    ]