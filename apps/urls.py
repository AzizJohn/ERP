from django.urls import path, include


urlpatterns = [
    path('personnel/', include('apps.personnel.urls')),
    path('internships/', include('apps.internships.urls')),
    path('projects/', include('apps.projects.urls')),
    path('events/', include('apps.events.urls')),
    path('attendance/', include('apps.attendance.urls')),
    path('inventory/', include('apps.inventories.urls')),

]
