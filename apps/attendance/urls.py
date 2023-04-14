from django.urls import path
from .api_endpoints import attendance
urlpatterns = [
    path('list/', attendance.AttendanceListView.as_view(), name='attendance-list'),
    path('create/', attendance.AttendanceCreateView.as_view(), name='attendance-create'),

]
