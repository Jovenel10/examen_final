
from django.urls import path
from gestionbiblio import views

urlpatterns = [
    path('', views.home, name='home'),  # URL de la page d'accueil
    path('livre/<int:livre_id>/', views.livre, name='livre_detail'),  # URL pour les détails d'un livre spécifique
    path('ajout_livre/', views.ajout_livre, name='ajout_livre'),  # URL pour ajouter un nouveau livre
    path('modifier_livre/<int:livre_id>/', views.modifier_livre, name='modifier_livre'),  # URL pour modifier un livre
    path('supprimer_livre/<int:livre_id>/', views.supprimer_livre, name='supprimer_livre'),  # URL pour supprimer un livre
]
