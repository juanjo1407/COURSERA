from juanjo1407.contrib import admin
from juanjo1407.urls import path, include

urlpatterns = [
    path('', include('app.urls')),
]
