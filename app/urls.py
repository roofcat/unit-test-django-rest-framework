from django.conf.urls import url
from django.contrib import admin


from rest_framework.authtoken.views import obtain_auth_token


from todos.views import TodoApiView


urlpatterns = [
    url(r'^api-auth/$', obtain_auth_token),
    url(r'^todos/$', TodoApiView.as_view(), name='todos'),
    url(r'^todos(?P<id>\d+)/$', TodoApiView.as_view()),
    url(r'^admin/', admin.site.urls),
]
