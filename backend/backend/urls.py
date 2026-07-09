from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse
from django.views.static import serve
from rest_framework import routers
from api import views
import os

router = routers.DefaultRouter()
router.register('tasks', views.TaskView, 'task')

urlpatterns = [
    path('', lambda request: HttpResponse('<html><body>Taski<script src="/static/js/main.js"></script></body></html>')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('static/js/main.js', lambda request: HttpResponse('// Taski', content_type='application/javascript')),
]
