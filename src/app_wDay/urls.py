from django.urls import path
from .views import palabra_del_dia

app_name = 'app_wDay'

urlpatterns = [
    path("", palabra_del_dia, name="palabra_del_dia"),
]
