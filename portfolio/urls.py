# urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'about', views.AboutViewSet, basename='about')
router.register(r'skills', views.SkillViewSet, basename='skill')
router.register(r'projects', views.ProjectViewSet, basename='project')
router.register(r'experience', views.ExperienceViewSet, basename='experience')
router.register(r'education', views.EducationViewSet, basename='education')
router.register(r'contact', views.ContactViewSet, basename='contact')
router.register(r'blog', views.BlogViewSet, basename='blog')
router.register(r'testimonials', views.TestimonialViewSet, basename='testimonial')
router.register(r'services', views.ServiceViewSet, basename='service')
router.register(r'hero', views.HeroViewSet, basename='hero')

# <<< NEW ROUTE ADDED HERE >>>
router.register(r'contact-details', views.ContactDetailsViewSet, basename='contact-details')

urlpatterns = [
    path('', include(router.urls)),
]