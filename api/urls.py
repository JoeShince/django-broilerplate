from rest_framework import routers

from api.views import SampleViewSets

router = routers.DefaultRouter()
router.register(r'test', SampleViewSets, basename='test')
