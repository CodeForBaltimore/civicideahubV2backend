from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateView
from .views import DetailsView 


urlpatterns = {
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^ideas/$', CreateView.as_view(), name="create"),
    url(r'^ideas/(?P<pk>[0-9]+)/$',
        DetailsView.as_view(), name="details")
}

urlpatterns = format_suffix_patterns(urlpatterns)