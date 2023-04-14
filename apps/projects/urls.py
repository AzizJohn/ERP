from django.urls import path

from .api_endpoints import project

urlpatterns = [
    path('list/', project.ProjectListView.as_view(), name='project-list'),
    path('create/', project.ProjectCreateView.as_view(), name='project-create'),
    path('update/<int:pk>/', project.ProjectUpdateView.as_view(), name='project-update'),
    path('delete/<int:pk>/', project.ProjectDestroyView.as_view(), name='project-delete'),
    path('retrieve/<int:pk>/', project.ProjectDetailView.as_view(), name='project-retrieve'),

]
