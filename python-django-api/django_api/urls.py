"""
URL configuration for django_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import re_path
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
import json

@api_view(['GET', ])
def healthcheck(request):
    return Response("OK")

employees_list = [
    { 'Id': 1, 'Firstname': "John", 'Lastname': "Doe" },
    { 'Id': 2, 'Firstname': "Peter", 'Lastname': "Parker" },
    { 'Id': 3, 'Firstname': "Tony", 'Lastname': "Stark" }
]

@api_view(['GET', 'POST'])
def employees(request):
    if request.method == 'POST':
        employees_list.append(json.loads(request.body))

    return JsonResponse(employees_list, safe=False)

urlpatterns = [
    re_path(r'^healthcheck/$', healthcheck),
    re_path(r'^employees/$', employees)
]
