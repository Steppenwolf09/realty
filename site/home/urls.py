"""reality URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django.conf.urls.static import static
from . import views
from .models import *
from home.views import SearchResultsView, FilterResultsView
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from rest_framework.renderers import JSONRenderer



class HouseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = House
        fields = ['name', 'descrip']


house=House.objects.all().first()
serializer=HouseSerializer(house)
json = JSONRenderer().render(serializer.data)
print("pop")
print(json)
print(serializer)


# ViewSets define the view behavior.
class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'houses', HouseViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', views.mainpage, name="mainpage"),
    url(r'^6', views.detail, name="detail"),
    url(r'^hati', views.allhouses, name="allhouses"),
    url(r'^createob', views.create, name="create"),
    url(r'^(?P<id_h>\d+)$', views.hata, name="hata"),
    url('^search', SearchResultsView.as_view(), name='search_results'),
    url('^filter', FilterResultsView.as_view(), name='filter'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
