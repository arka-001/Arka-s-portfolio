# views.py

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import (
    About, Skill, Project, Experience, Education, 
    Contact, Blog, Testimonial, Service, Hero
)
from .serializers import (
    AboutSerializer, SkillSerializer, ProjectSerializer, ExperienceSerializer,
    EducationSerializer, ContactSerializer, BlogSerializer, TestimonialSerializer,
    ServiceSerializer, HeroSerializer, ProjectListSerializer, SkillListSerializer,
    ExperienceListSerializer, BlogListSerializer, HeroListSerializer,
    ContactDetailsSerializer  # <-- IMPORT ADDED
)

class AboutViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = About.objects.filter(is_active=True)
    serializer_class = AboutSerializer

class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Skill.objects.filter(is_active=True)
    serializer_class = SkillSerializer
    
    def get_serializer_class(self):
        if self.action == 'list':
            return SkillListSerializer
        return SkillSerializer
    
    @action(detail=False, methods=['get'])
    def categories(self, request):
        categories = Skill.objects.filter(is_active=True).values_list('category', flat=True).distinct()
        return Response(categories)

class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.filter(is_active=True)

    def get_serializer_class(self):
        if self.action == 'list':
            return ProjectListSerializer
        return ProjectSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def get_queryset(self):
        queryset = Project.objects.filter(is_active=True)
        featured = self.request.query_params.get('featured')
        project_type = self.request.query_params.get('type')

        if featured:
            queryset = queryset.filter(featured=True)
        if project_type:
            queryset = queryset.filter(project_type=project_type)

        return queryset

    @action(detail=False, methods=['get'])
    def featured(self, request):
        featured_projects = Project.objects.filter(featured=True, is_active=True)
        serializer = ProjectListSerializer(featured_projects, many=True, context=self.get_serializer_context())
        return Response(serializer.data)

class ExperienceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Experience.objects.filter(is_active=True)
    
    def get_serializer_class(self):
        if self.action == 'list':
            return ExperienceListSerializer
        return ExperienceSerializer
    
    def get_queryset(self):
        return Experience.objects.filter(is_active=True).order_by('-start_date', 'order')

class EducationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Education.objects.filter(is_active=True)
    serializer_class = EducationSerializer
    
    def get_queryset(self):
        return Education.objects.filter(is_active=True).order_by('-start_date', 'order')

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    
    def get_queryset(self):
        # Only allow admins to see all contacts
        if self.request.user.is_staff:
            return Contact.objects.all()
        return Contact.objects.none()

class BlogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Blog.objects.filter(published=True)
    
    def get_serializer_class(self):
        if self.action == 'list':
            return BlogListSerializer
        return BlogSerializer
    
    def get_queryset(self):
        queryset = Blog.objects.filter(published=True)
        search = self.request.query_params.get('search')
        
        if search:
            queryset = queryset.filter(title__icontains=search) | queryset.filter(content__icontains=search)
            
        return queryset
    
    @action(detail=False, methods=['get'])
    def featured(self, request):
        featured_posts = Blog.objects.filter(featured=True, published=True)
        serializer = BlogListSerializer(featured_posts, many=True)
        return Response(serializer.data)

class TestimonialViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Testimonial.objects.filter(is_active=True)
    serializer_class = TestimonialSerializer
    
    def get_queryset(self):
        return Testimonial.objects.filter(is_active=True).order_by('order', '-created_at')

class ServiceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Service.objects.filter(is_active=True)
    serializer_class = ServiceSerializer
    
    def get_queryset(self):
        return Service.objects.filter(is_active=True).order_by('order', 'title')

class HeroViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = HeroSerializer
    
    def get_queryset(self):
        return Hero.objects.filter(is_active=True)
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset.exists():
            serializer = self.get_serializer(queryset.first())
            return Response([serializer.data])
        return Response([])
    
    @action(detail=False, methods=['get'])
    def active(self, request):
        active_hero = Hero.objects.filter(is_active=True).first()
        if active_hero:
            serializer = HeroSerializer(active_hero)
            return Response(serializer.data)
        return Response({}, status=status.HTTP_404_NOT_FOUND)

# <<< NEW VIEWSET ADDED HERE >>>
class ContactDetailsViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that provides contact details from the active 'About' profile.
    This provides a single object, not a list.
    """
    serializer_class = ContactDetailsSerializer

    def get_queryset(self):
        # We only care about the single active 'About' object
        return About.objects.filter(is_active=True)

    def list(self, request, *args, **kwargs):
        # Override the default 'list' action to return a single object
        active_profile = self.get_queryset().first()
        if active_profile:
            serializer = self.get_serializer(active_profile)
            return Response(serializer.data)
        # Return an empty object if no active profile is found
        return Response({})