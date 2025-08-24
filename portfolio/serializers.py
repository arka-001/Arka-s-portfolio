# serializers.py

from rest_framework import serializers
from .models import (
    About, Skill, Project, Experience, Education, 
    Contact, Blog, Testimonial, Service, Hero
)

class AboutSerializer(serializers.ModelSerializer):
    profile_image_url = serializers.SerializerMethodField()
    class Meta:
        model = About
        fields = '__all__'
    def get_profile_image_url(self, obj):
        request = self.context.get('request')
        if obj.profile_image and request:
            return request.build_absolute_uri(obj.profile_image.url)
        return None

class SkillSerializer(serializers.ModelSerializer):
    category_display = serializers.CharField(source='get_category_display', read_only=True)
    
    class Meta:
        model = Skill
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    technologies = SkillSerializer(many=True, read_only=True)
    project_type_display = serializers.CharField(source='get_project_type_display', read_only=True)
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = Project
        fields = '__all__'
    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None

class ExperienceSerializer(serializers.ModelSerializer):
    technologies_used = SkillSerializer(many=True, read_only=True)
    
    class Meta:
        model = Experience
        fields = '__all__'

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    featured_image_url = serializers.SerializerMethodField()
    class Meta:
        model = Blog
        fields = '__all__'
    def get_featured_image_url(self, obj):
        request = self.context.get('request')
        if obj.featured_image and request:
            return request.build_absolute_uri(obj.featured_image.url)
        return None

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = '__all__'

# Nested serializers for related data
class ProjectListSerializer(serializers.ModelSerializer):
    technologies = SkillSerializer(many=True, read_only=True)
    project_type_display = serializers.CharField(source='get_project_type_display', read_only=True)
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = Project
        fields = ['id', 'title', 'short_description', 'project_type', 'project_type_display', 
                 'technologies', 'image_url', 'github_url', 'live_url', 'demo_url', 'featured', 
                 'created_at']
    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None

class SkillListSerializer(serializers.ModelSerializer):
    category_display = serializers.CharField(source='get_category_display', read_only=True)
    
    class Meta:
        model = Skill
        fields = ['id', 'name', 'category', 'category_display', 'proficiency', 'icon', 'color']

class ExperienceListSerializer(serializers.ModelSerializer):
    technologies_used = SkillSerializer(many=True, read_only=True)
    
    class Meta:
        model = Experience
        fields = ['id', 'company', 'position', 'location', 'start_date', 'end_date', 
                 'current', 'description', 'technologies_used', 'company_logo']

class BlogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'title', 'slug', 'excerpt', 'featured_image', 'author', 
                 'tags', 'views', 'created_at', 'published_at']

class HeroListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = ['id', 'name', 'tagline', 'description', 'resume_url', 'contact_email']

# <<< NEW SERIALIZER ADDED HERE >>>
class ContactDetailsSerializer(serializers.ModelSerializer):
    """
    A specific serializer to expose only the contact details from the About model.
    """
    class Meta:
        model = About
        fields = [
            'email', 'phone', 'location', 
            'github', 'linkedin', 'twitter', 'website'
        ]