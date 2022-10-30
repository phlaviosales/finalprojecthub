from django.urls import path
from hub.views import index

urlpatterns = [
    path('', index)
    path('', include('hub.urls'))
]