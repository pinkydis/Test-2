from django.conf.urls import url

from test_app.views import MainPageView

app_name = 'test_app'

urlpatterns = [
    url(r'^$', MainPageView.as_view(), name='index'),
    url(r'^(.*)/$', MainPageView.as_view(), name='index'),
]