from django.urls import path
from mainapp import views as mainapp_views

app_name = 'main'

urlpatterns = [
    path('', mainapp_views.main),
    path('authenticated/', mainapp_views.authenticated)
]
