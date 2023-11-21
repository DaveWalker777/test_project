from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('management', views.management, name='management'),
    path('ranks', views.ranks, name='ranks'),
    path('create_rank', views.create_rank, name='create_rank'),
    path('create_person', views.create_person, name='create_person'),
    path('update_person/<person_id>', views.update_person, name='update_person'),
    path('delete_person/<person_id>', views.delete_person, name='delete_person'),
    path('update_rank/<rank_id>', views.update_rank, name='update_rank'),
    path('delete_rank/<rank_id>', views.delete_rank, name='delete_rank'),
]