from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'profile', views.ProfileViewSet, basename='profile')
router.register(r'contact', views.ContactViewSet, basename='contact')
router.register(r'skills', views.SkillsViewSet, basename='skills')
router.register(r'testimonials', views.TestimonialViewSet, basename='testimonial')
router.register(r'contact-me', views.ContactMeViewSet, basename='contact-me')


urlpatterns = [
    path('api/', include(router.urls)),
]
