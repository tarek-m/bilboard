from django.conf.urls import url
from django.conf.urls import include



from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    url(r'^index$', views.index, name='index'),
    # url(r'^signup/$', views.signup, name='signup'),

 

]