from django.conf.urls import url, include
from snippets import views
from rest_framework import routers
from snippets.serializers import SnippetsViewSet
router = routers.DefaultRouter()
router.register(r'ui_snippets', SnippetsViewSet)

urlpatterns = [
	url(r'^', include(router.urls)),
	url(r'^snippets/$', views.snippet_list, name="snippets_list"),
	url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail, name="snippets_details"),
]