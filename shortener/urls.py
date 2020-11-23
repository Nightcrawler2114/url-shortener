from django.urls import path

from shortener import views


urlpatterns = [
    path('', views.UrlObjectListView.as_view(), name='list_view'),
    path('create/', views.UrlObjectCreateView.as_view(), name='create_view'),
    path('increase-visitors/', views.increase_visitors_counter, name='increase_visitors'),
]