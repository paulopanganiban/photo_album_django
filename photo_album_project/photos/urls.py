from django.urls import path
from . import views
from .views import PostDashboardListView, PostDashboardDetailView
app_name = "photos"

urlpatterns = [
    path('', PostDashboardListView.as_view(), name='list'),
    path('<slug:slug>/', PostDashboardDetailView.as_view(), name='detail'),
]

# <app>/<model>_<viewtype>.html