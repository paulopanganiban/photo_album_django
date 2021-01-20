from django.urls import path
from . import views
from .views import (
    PostDashboardListView, 
    PostDashboardDetailView, 
    PostDashboardCreateView, 
    PostDashboardUpdateView,
    PostDashboardDeleteView,)
app_name = "photos"

urlpatterns = [
    #photo/
    path('', PostDashboardListView.as_view(), name='list'),
    path('create/', PostDashboardCreateView.as_view(), name='create'),
    path('<slug:slug>/', PostDashboardDetailView.as_view(), name='detail'),
    path('<slug:slug>/update/', PostDashboardUpdateView.as_view(), name='update'),
    path('<slug:slug>/delete/', PostDashboardDeleteView.as_view(), name='delete'),
]

# <app>/<model>_<viewtype>.html