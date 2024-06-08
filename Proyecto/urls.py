from django.contrib import admin
from django.urls import path
from Historia import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pacientes/', views.pacientes_view, name='pacientes'),
    path('pacientes/nuevo/', views.create_patient, name='create_patient'),
    path('pacientes/<str:ci>/eliminar/', views.delete_patient, name='delete_patient'),
    path('pacientes/<str:ci>/editar/', views.edit_patient, name='edit_patient'),
    path('pacientes/<str:ci>/historias/', views.patient_histories, name='patient_histories'),
    path('historial/create/', views.historial_create, name='historial_create'),
    
]
