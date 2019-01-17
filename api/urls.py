from django.urls import include, path
from django.conf.urls import url
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('rest-auth/', include('rest_auth.urls')),
    url(r'^', include(router.urls)),
    url(r'^api-token-auth/', obtain_jwt_token)
    #url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
