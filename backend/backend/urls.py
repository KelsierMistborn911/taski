from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register('tasks', views.TaskView, 'task')

urlpatterns = [
    path('', lambda request: HttpResponse('<html><body>Taski<script src="/static/js/main.js"></script></body></html>')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
