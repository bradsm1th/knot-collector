from django.urls import path

from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('knots/', views.knots_index, name='index'),
  path('knots/<int:knot_id>/', views.knots_detail, name='detail'),
]