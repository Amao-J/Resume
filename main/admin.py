from django.contrib import admin
from . models import (
    UserProfile,
    ContactProfile,
    Testimonials,
    Media,
    Portfolio,
    Blog,
    Certificate,Skills
)

# Register your models here.

@admin.register(UserProfile)

class UserProfileAdmin(admin.ModelAdmin):
    list_display=('id','user')
    
@admin.register( Media)

class MediaAdmin(admin.ModelAdmin):
    list_display=('id','name')
    
@admin.register(Certificate)

class CertificateAdmin(admin.ModelAdmin):
    list_display=('id','name')
    
    
@admin.register(ContactProfile)
class ContactProfileAdmin(admin.ModelAdmin):
    list_display=('id','timestamp','name',)
   
    
@admin.register(Testimonials)
class TestimonailsAdmin(admin.ModelAdmin):
    list_display=('id','name','is_active')
    
@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display=('id','name','is_active')
    readonly_fields=('slug',)
    
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display=('id','name','is_active')
    readonly_fields=('slug',)
    
@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display=('id','name','score')
    
    



    