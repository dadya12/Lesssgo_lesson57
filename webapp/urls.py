from django.urls import path
from webapp.templates.views.project_views import HomePageView, DetailPageView, CreatePageView, EditPageView, \
    DeletePageView, UpdateUserView
from webapp.templates.views.task_views import TaskCreateView, TaskDetailView, TaskEditView, TaskDeleteView

app_name = 'webapp'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('detail/<int:pk>/', DetailPageView.as_view(), name='detail'),
    path('create/', CreatePageView.as_view(), name='create'),
    path('edit/<int:pk>/', EditPageView.as_view(), name='edit'),
    path('delete/<int:pk>/', DeletePageView.as_view(), name='delete'),
    path('task/<int:pk>/create', TaskCreateView.as_view(), name='task_create'),
    path('task/<int:pk>/detail', TaskDetailView.as_view(), name='task_detail'),
    path('task/<int:pk>/update', TaskEditView.as_view(), name='task_update'),
    path('task/<int:pk>/delete', TaskDeleteView.as_view(), name='task_delete'),
    path('projects/<int:pk>/users/update/', UpdateUserView.as_view(), name='update_user'),
]
