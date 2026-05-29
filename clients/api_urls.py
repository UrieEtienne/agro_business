from rest_framework.routers import DefaultRouter

from .api_views import ClientViewSet


router = DefaultRouter()

router.register(

    r'clients',

    ClientViewSet

)

urlpatterns = router.urls