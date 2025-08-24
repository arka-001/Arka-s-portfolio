from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from django.utils.safestring import mark_safe
from .models import (
    About, Skill, Project, Experience, Education, 
    Contact, Blog, Testimonial, Service, Hero
)

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'email', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'title', 'email']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'title', 'description', 'profile_image')
        }),
        ('Contact Information', {
            'fields': ('email', 'phone', 'location')
        }),
        ('Social Links', {
            'fields': ('github', 'linkedin', 'twitter', 'website'),
            'classes': ('collapse',)
        }),
        ('Files', {
            'fields': ('resume',),
            'classes': ('collapse',)
        }),
        ('Status', {
            'fields': ('is_active', 'created_at', 'updated_at')
        }),
    )

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency', 'color_display', 'is_active', 'order']
    list_filter = ['category', 'is_active', 'created_at']
    search_fields = ['name']
    list_editable = ['proficiency', 'order', 'is_active']
    ordering = ['order', 'name']
    
    def color_display(self, obj):
        return format_html(
            '<span style="color: {}; font-weight: bold;">{}</span>',
            obj.color,
            obj.color
        )
    color_display.short_description = 'Color'

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'project_type', 'featured', 'is_active', 'order', 'technologies_display', 'created_at']
    list_filter = ['project_type', 'featured', 'is_active', 'created_at']
    search_fields = ['title', 'description']
    list_editable = ['featured', 'is_active', 'order']
    filter_horizontal = ['technologies']
    ordering = ['-featured', 'order', '-created_at']
    
    def technologies_display(self, obj):
        return ", ".join([tech.name for tech in obj.technologies.all()[:3]])
    technologies_display.short_description = 'Technologies'
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'short_description', 'project_type')
        }),
        ('Media & Links', {
            'fields': ('image', 'github_url', 'live_url', 'demo_url')
        }),
        ('Technologies', {
            'fields': ('technologies',)
        }),
        ('Settings', {
            'fields': ('featured', 'is_active', 'order')
        }),
    )

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['position', 'company', 'location', 'start_date', 'end_date', 'current', 'is_active', 'order']
    list_filter = ['current', 'is_active', 'start_date', 'created_at']
    search_fields = ['position', 'company', 'description']
    list_editable = ['is_active', 'order']
    filter_horizontal = ['technologies_used']
    ordering = ['-start_date', 'order']
    
    fieldsets = (
        ('Position Details', {
            'fields': ('company', 'position', 'location')
        }),
        ('Duration', {
            'fields': ('start_date', 'end_date', 'current')
        }),
        ('Description', {
            'fields': ('description',)
        }),
        ('Technologies', {
            'fields': ('technologies_used',)
        }),
        ('Media', {
            'fields': ('company_logo',)
        }),
        ('Settings', {
            'fields': ('is_active', 'order')
        }),
    )

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'field_of_study', 'institution', 'start_date', 'end_date', 'current', 'is_active', 'order']
    list_filter = ['current', 'is_active', 'start_date', 'created_at']
    search_fields = ['degree', 'field_of_study', 'institution']
    list_editable = ['is_active', 'order']
    ordering = ['-start_date', 'order']
    
    fieldsets = (
        ('Education Details', {
            'fields': ('institution', 'degree', 'field_of_study')
        }),
        ('Duration', {
            'fields': ('start_date', 'end_date', 'current')
        }),
        ('Additional Information', {
            'fields': ('grade', 'description')
        }),
        ('Media', {
            'fields': ('institution_logo',)
        }),
        ('Settings', {
            'fields': ('is_active', 'order')
        }),
    )

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'is_read', 'created_at']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'subject', 'message']
    list_editable = ['is_read']
    readonly_fields = ['created_at']
    ordering = ['-created_at']
    
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email', 'phone')
        }),
        ('Message', {
            'fields': ('subject', 'message')
        }),
        ('Status', {
            'fields': ('is_read', 'created_at')
        }),
    )
    
    actions = ['mark_as_read', 'mark_as_unread']
    
    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)
    mark_as_read.short_description = "Mark selected messages as read"
    
    def mark_as_unread(self, request, queryset):
        queryset.update(is_read=False)
    mark_as_unread.short_description = "Mark selected messages as unread"

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published', 'featured', 'views', 'created_at']
    list_filter = ['published', 'featured', 'created_at', 'published_at']
    search_fields = ['title', 'content', 'tags']
    list_editable = ['published', 'featured']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['views', 'created_at', 'updated_at']
    ordering = ['-published_at', '-created_at']
    
    fieldsets = (
        ('Content', {
            'fields': ('title', 'slug', 'content', 'excerpt')
        }),
        ('Media', {
            'fields': ('featured_image',)
        }),
        ('Meta Information', {
            'fields': ('author', 'tags')
        }),
        ('Publication', {
            'fields': ('published', 'featured', 'published_at')
        }),
        ('Statistics', {
            'fields': ('views', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    actions = ['publish_posts', 'unpublish_posts']
    
    def publish_posts(self, request, queryset):
        queryset.update(published=True)
    publish_posts.short_description = "Publish selected posts"
    
    def unpublish_posts(self, request, queryset):
        queryset.update(published=False)
    unpublish_posts.short_description = "Unpublish selected posts"

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'company', 'rating', 'is_active', 'order']
    list_filter = ['rating', 'is_active', 'created_at']
    search_fields = ['name', 'position', 'company', 'content']
    list_editable = ['rating', 'is_active', 'order']
    ordering = ['order', '-created_at']
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'position', 'company', 'image')
        }),
        ('Testimonial', {
            'fields': ('content', 'rating')
        }),
        ('Settings', {
            'fields': ('is_active', 'order')
        }),
    )

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'color_display', 'is_active', 'order']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'description']
    list_editable = ['is_active', 'order']
    ordering = ['order', 'title']
    
    def color_display(self, obj):
        return format_html(
            '<span style="color: {}; font-weight: bold;">{}</span>',
            obj.color,
            obj.color
        )
    color_display.short_description = 'Color'
    
    fieldsets = (
        ('Service Information', {
            'fields': ('title', 'description')
        }),
        ('Styling', {
            'fields': ('icon', 'color')
        }),
        ('Settings', {
            'fields': ('is_active', 'order')
        }),
    )

@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ['name', 'tagline', 'contact_email', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'tagline', 'description']
    list_editable = ['is_active']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Hero Content', {
            'fields': ('name', 'tagline', 'description')
        }),
        ('Contact Information', {
            'fields': ('contact_email', 'resume_url')
        }),
        ('Status', {
            'fields': ('is_active', 'created_at', 'updated_at')
        }),
    )
    
    def has_delete_permission(self, request, obj=None):
        if obj and obj.is_active:
            active_count = Hero.objects.filter(is_active=True).count()
            if active_count <= 1:
                return False
        return True

# Customize admin site
admin.site.site_header = "Arka Portfolio Admin"
admin.site.site_title = "Portfolio Admin"
admin.site.index_title = "Welcome to Arka Portfolio Administration"