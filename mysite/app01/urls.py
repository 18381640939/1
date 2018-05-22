from django.conf.urls import url,include
from django.contrib import admin
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import staticfiles
admin.autodiscover()

urlpatterns = (
    url(r'^index/$',views.index,name='index'),
    url(r'^login/$',views.login,name='login'),
    url(r'^regist/$',views.regist,name='regist'),
    url(r'^table/$',views.table,name='table'),
    url(r'^erweima/$',views.erweima,name='erweima'),
    url(r'^admin/', admin.site.urls),
)
