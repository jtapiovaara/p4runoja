from django.urls import path
from . import views

urlpatterns = [
    path('', views.runoLista, name='runoLista'),
    path('uusi/', views.runoUusi, name='runoUusi'),
    # path('korjaa/<int:runo_id>', views.runoKorjaa),
    # path('poista/<int:runo_id>', views.runoPoista)
    path('printed/', views.html_to_pdf_view, name='printruno'),
    path('printed/<int:pk>', views.html_to_pdf_one_view, name='printoneruno')
    ]