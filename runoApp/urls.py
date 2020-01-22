from django.urls import path
from . import views

urlpatterns = [
    path('', views.runoLista, name='runoLista'),
    path('uusi/', views.runoUusi, name='runoUusi')
    # path('korjaa/<int:runo_id>', views.runoKorjaa),
    # path('poista/<int:runo_id>', views.runoPoista)
    ]

# urlpatterns = [
#     path('', views.library, name='library'),
#     path('uusikirja/', views.uusikirja, name='uusikirja'),
#     path('update/<int:traincrud_id>', views.update_book),
#     path('delete/<int:traincrud_id>', views.delete_book)
#     ]
