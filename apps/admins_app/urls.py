from django.conf.urls import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import AdminLoginAPI, reset_page

router = DefaultRouter()
router.register(r'function', FunctionAPI, basename='function'),
router.register(r'skill', SkillAPI, basename='skill'),

urlpatterns = [
    path('login/', AdminLoginAPI.as_view({'post': 'login'})),
    url('', include(router.urls)),
]