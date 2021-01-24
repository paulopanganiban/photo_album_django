from django.urls import path
from .views import (
    PostDashboardListView, 
    PostDashboardDetailView, 
    PostDashboardCreateView, 
    PostDashboardUpdateView,
    PostDashboardDeleteView,
    TestCreateView,)
app_name = "photos"

urlpatterns = [
    #photo/
    path('', PostDashboardListView.as_view(), name='list'),
    path('create/', PostDashboardCreateView.as_view(), name='create'),
    path('test/', TestCreateView.as_view(), name='test'),
    path('post/<slug:slug>/', PostDashboardDetailView.as_view(), name='detail'),
    path('post/<slug:slug>/update/', PostDashboardUpdateView.as_view(), name='update'),
    path('post/<slug:slug>/delete/', PostDashboardDeleteView.as_view(), name='delete'),
]

# <app>/<model>_<viewtype>.html