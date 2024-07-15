from django.urls import path
from webapp.templates.views.project_views import HomePageView, DetailPageView, CreatePageView, EditPageView, DeletePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('detail/<int:pk>/', DetailPageView.as_view(), name='detail'),
    path('create/', CreatePageView.as_view(), name='create'),
    path('edit/<int:pk>/', EditPageView.as_view(), name='edit'),
    path('delete/<int:pk>/', DeletePageView.as_view(), name='delete'),
]
