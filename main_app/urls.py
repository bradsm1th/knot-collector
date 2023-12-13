from django.urls import path

from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('knots/', views.knots_index, name='index'),
  path('knots/<int:knot_id>/', views.knots_detail, name='detail'),
  path('knots/create/', views.KnotCreate.as_view(), name='knots_create'),
  path('knots/<int:pk>/update/', views.KnotUpdate.as_view(), name='knots_update'),
  path('knots/<int:pk>/delete/', views.KnotDelete.as_view(), name='knots_delete'),
]