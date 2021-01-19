from django.urls import path
from . import views
from .views import PostDashboardListView, PostDashboardDetailView, PostDashboardCreateView
app_name = "photos"

urlpatterns = [
    #photo/
    path('', PostDashboardListView.as_view(), name='list'),
    path('create/', PostDashboardCreateView.as_view(), name='create'),
    path('<slug:slug>/', PostDashboardDetailView.as_view(), name='detail'),
]

# <app>/<model>_<viewtype>.html