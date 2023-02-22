from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSets, base_name='hello-viewSet')

urlpatterns = [
	path('hello-view/', views.Hello.as_view()),
	path('', include(router.urls))
]