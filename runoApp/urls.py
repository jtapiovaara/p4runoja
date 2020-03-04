from django.urls import path
from . import views

urlpatterns = [
    path('', views.RunoList.as_view(), name='runolista'),
    path('lue/<pk>', views.RunoRead.as_view(), name='runolue'),
    path('uusi/', views.RunoCreate.as_view(), name='runouusi'),
    path('korjaa/<pk>', views.RunoEdit.as_view(), name='runokorjaa'),
    path('poista/<pk>', views.RunoDelete.as_view(), name='runopoista'),
    path('printed/', views.html_to_pdf_view, name='printruno'),
    path('printed/<int:pk>', views.html_to_pdf_one_view, name='printoneruno')
    ]