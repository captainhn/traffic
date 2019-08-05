from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^main/$',views.main),
    url(r'^main/location/$',views.location),
    url(r'^main/history/$',views.history),
    url(r'^main/future/$',views.future),

]