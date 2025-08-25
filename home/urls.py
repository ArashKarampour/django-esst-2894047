from django.urls import path
from . import views


urlpatterns = [
    path('home', views.HomeView.as_view()),  # Class Based View for home
    # path('home', views.home),
    path('authorized', views.AuthorizedView.as_view()),
    # path('authorized', views.authorized),
]