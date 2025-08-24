from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import date
from portfolio.models import About, Skill, Project, Experience, Education, Service, Testimonial, Blog

class Command(BaseCommand):
    help = 'Populate the database with sample portfolio data'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample portfolio data...')
        
        # Create About
        about, created = About.objects.get_or_create(
            name="Arka Maitra",
            defaults={
                'title': "Full Stack Developer & UI/UX Designer",
                'description': "I'm a passionate Full Stack Developer with expertise in modern web technologies.",
                'email': "arkamaitra001@gmail.com",
                'phone': "+91 9876543210",
                'location': "Kolkata, West Bengal, India",
                'github': "https://github.com/arkamaitra",
                'linkedin': "https://linkedin.com/in/arkamaitra",
                'is_active': True
            }
        )
        if created:
            self.stdout.write(f'Created About: {about.name}')
        
        # Create Skills
        skills_data = [
            {'name': 'Python', 'category': 'programming', 'proficiency': 90, 'icon': 'fab fa-python', 'color': '#3776AB'},
            {'name': 'JavaScript', 'category': 'programming', 'proficiency': 85, 'icon': 'fab fa-js-square', 'color': '#F7DF1E'},
            {'name': 'Django', 'category': 'framework', 'proficiency': 90, 'icon': 'fab fa-python', 'color': '#092E20'},
            {'name': 'React', 'category': 'framework', 'proficiency': 85, 'icon': 'fab fa-react', 'color': '#61DAFB'},
            {'name': 'MySQL', 'category': 'database', 'proficiency': 85, 'icon': 'fas fa-database', 'color': '#4479A1'},
        ]
        
        for skill_data in skills_data:
            skill, created = Skill.objects.get_or_create(
                name=skill_data['name'],
                defaults=skill_data
            )
            if created:
                self.stdout.write(f'Created Skill: {skill.name}')
        
        # Create Projects
        projects_data = [
            {
                'title': 'E-Commerce Platform',
                'description': 'A full-featured e-commerce platform built with Django and React.',
                'short_description': 'Modern e-commerce platform with Django backend and React frontend',
                'project_type': 'web',
                'github_url': 'https://github.com/arkamaitra/ecommerce-platform',
                'live_url': 'https://ecommerce-demo.arkamaitra.com',
                'featured': True
            },
            {
                'title': 'Task Management App',
                'description': 'A collaborative task management application with real-time updates.',
                'short_description': 'Collaborative task management with real-time updates',
                'project_type': 'web',
                'github_url': 'https://github.com/arkamaitra/task-manager',
                'live_url': 'https://task-manager.arkamaitra.com',
                'featured': True
            }
        ]
        
        for project_data in projects_data:
            project, created = Project.objects.get_or_create(
                title=project_data['title'],
                defaults=project_data
            )
            if created:
                self.stdout.write(f'Created Project: {project.title}')
        
        # Create Experience
        experience_data = [
            {
                'company': 'Tech Solutions Inc.',
                'position': 'Senior Full Stack Developer',
                'location': 'Kolkata, India',
                'start_date': date(2022, 1, 1),
                'current': True,
                'description': 'Leading development of web applications using Django, React, and modern cloud technologies.'
            }
        ]
        
        for exp_data in experience_data:
            experience, created = Experience.objects.get_or_create(
                company=exp_data['company'],
                position=exp_data['position'],
                defaults=exp_data
            )
            if created:
                self.stdout.write(f'Created Experience: {experience.position} at {experience.company}')
        
        # Create Education
        education_data = [
            {
                'institution': 'Indian Institute of Technology',
                'degree': 'Bachelor of Technology',
                'field_of_study': 'Computer Science and Engineering',
                'start_date': date(2015, 8, 1),
                'end_date': date(2019, 5, 31),
                'current': False,
                'grade': '8.5/10',
                'description': 'Graduated with honors. Completed capstone project on machine learning applications.'
            }
        ]
        
        for edu_data in education_data:
            education, created = Education.objects.get_or_create(
                institution=edu_data['institution'],
                degree=edu_data['degree'],
                defaults=edu_data
            )
            if created:
                self.stdout.write(f'Created Education: {education.degree} from {education.institution}')
        
        # Create Services
        services_data = [
            {
                'title': 'Web Development',
                'description': 'Full-stack web development using modern technologies like Django, React, and Node.js.',
                'icon': 'fas fa-code',
                'color': '#007bff'
            },
            {
                'title': 'Mobile App Development',
                'description': 'Cross-platform mobile application development using React Native and Flutter.',
                'icon': 'fas fa-mobile-alt',
                'color': '#28a745'
            }
        ]
        
        for service_data in services_data:
            service, created = Service.objects.get_or_create(
                title=service_data['title'],
                defaults=service_data
            )
            if created:
                self.stdout.write(f'Created Service: {service.title}')
        
        # Create Testimonials
        testimonials_data = [
            {
                'name': 'Sarah Johnson',
                'position': 'Project Manager',
                'company': 'Tech Solutions Inc.',
                'content': 'Arka is an exceptional developer who consistently delivers high-quality work.',
                'rating': 5
            }
        ]
        
        for testimonial_data in testimonials_data:
            testimonial, created = Testimonial.objects.get_or_create(
                name=testimonial_data['name'],
                company=testimonial_data['company'],
                defaults=testimonial_data
            )
            if created:
                self.stdout.write(f'Created Testimonial: {testimonial.name}')
        
        # Create Blog Posts
        blog_data = [
            {
                'title': 'Getting Started with Django REST Framework',
                'slug': 'getting-started-with-django-rest-framework',
                'content': 'Django REST Framework (DRF) is a powerful toolkit for building Web APIs.',
                'excerpt': 'Learn how to build powerful APIs with Django REST Framework',
                'author': 'Arka Maitra',
                'tags': 'Django, API, Python, Web Development',
                'published': True,
                'featured': True
            }
        ]
        
        for blog_data_item in blog_data:
            blog, created = Blog.objects.get_or_create(
                slug=blog_data_item['slug'],
                defaults=blog_data_item
            )
            if created:
                self.stdout.write(f'Created Blog Post: {blog.title}')
        
        self.stdout.write(
            self.style.SUCCESS('Successfully created sample portfolio data!')
        )
