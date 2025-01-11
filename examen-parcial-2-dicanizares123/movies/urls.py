from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:movie_id>/", views.movie_detail, name="display_moviedetails")
    #path("trainer/<int:trainer_id>/", views.trainer_detail, name="trainer"),

] 

