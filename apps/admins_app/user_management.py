from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ObjectDoesNotExist
from drf_yasg.utils import swagger_auto_schema
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from apps.admins_app.models import AdminUser, Skill, Function
