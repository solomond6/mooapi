from django.urls import path
from rest_framework.routers import DefaultRouter
from moove_apps.driver import views
from django.conf.urls import url, include

router = DefaultRouter()
router.register(r'vehicle-assignment', views.DriverVehicleAssignmentModelView, basename='vehicle-assignment')
router.register(r'plan-assignment', views.DriverPlanAssignmentModelView, basename='plan-assignment')
router.register(r'status-assignment', views.DriverStatusAssignmentModelView, basename='status-assignment')
router.register(r'driver-score-card', views.DriverScoreCardModelView, basename='driver-score-card')
router.register(r'vehicle-status-assignment', views.VehicleStatusModelView, basename='vehicle-status-assignment')
router.register(r'driver-infraction', views.InfractionRecordModelView, basename='driver-infraction')

urlpatterns = [
     path('virtual-info/', views.DriverVirtualAccountView.as_view(), name='virtual-info'),
     path('ussd-acount-info/', views.DriverGtbUssdAccountView.as_view(), name='ussd-acount-info'),
     path('ussd-acount-detail', views.DriverGtbAccountDetailView.as_view(), name='ussd-acount-detail'),
     path('available-vehicles/', views.AvailableDriversAPIlView.as_view(), name='available-vehicles'),
     path('plans/', views.PlanAPIlView.as_view(), name='plans'),
]
urlpatterns += router.urls

app_name = 'driver'
