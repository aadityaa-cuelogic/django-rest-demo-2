from django.conf.urls import url, include
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

from rest_framework import routers
# from snippets.serializers import SnippetsViewSet
# router = routers.DefaultRouter()
# router.register(r'ui_snippets', SnippetsViewSet)

urlpatterns = [
	# url(r'^', include(router.urls)),
	url(r'^snippets/$', views.SnippetList.as_view()),
	url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
	url(r'^users/$', views.UserList.as_view()),
	url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)