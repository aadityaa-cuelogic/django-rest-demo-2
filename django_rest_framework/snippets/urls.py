from django.conf.urls import url, include
from snippets.views import SnippetViewSet, UserViewSet, api_root
from rest_framework.routers import DefaultRouter
from rest_framework import renderers

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', SnippetViewSet)
router.register(r'users', UserViewSet)


urlpatterns = [
	url(r'^', include(router.urls)),
]