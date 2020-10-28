from django.conf.urls import url
from basic_app import views

# Template Tagging (app_name is a global variable)
app_name = 'basic_app'

# When you go to basic_app/anything, show these views
urlpatterns = [
    url(r'^relative/$',views.relative,name='relative'),
    url(r'^other/$',views.other,name='other'),
]
