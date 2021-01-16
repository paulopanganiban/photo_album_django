from django.urls import path
from . import views
from .views import PostListView, PostDashboardListView
app_name = "photos"

urlpatterns = [
    path('', PostDashboardListView.as_view(), name='dashboard'),
]

# <app>/<model>_<viewtype>.html