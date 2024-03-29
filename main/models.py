from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
# Create your models here.


class Skills(models.Model):
    class Meta:
        verbose_name_plural='Skills'
        verbose_name='Skill'
        
        
    name=models.CharField(max_length=20,blank=True,null=True)
    score=models.IntegerField(default=80,blank=True,null=True)
    image=models.FileField(blank=True,null=True,upload_to='skills' )
    is_key_skill=models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.name
    
    
class UserProfile(models.Model):
    class Meta:
        verbose_name_plural='User Profile'
        verbose_name='User Profile'
        
        
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar =models.ImageField(blank=True,null=True,upload_to='avatar')
    title=models.CharField(max_length=200,blank=True,null=True)
    bio=models.TextField(blank=True,null=True)
    skills=models.ManyToManyField(Skills,blank=True)
    cv=models.FileField(blank=True,null=True,upload_to='cv')

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    
class ContactProfile(models.Model):
    class Meta:
        verbose_name_plural='Contact Profiles'
        verbose_name='Contact profile'  
        ordering=["timestamp"]


    timestamp=models.DateField(auto_now_add=True)
    name=models.CharField(verbose_name='Name',max_length=100)
    email=models.EmailField(verbose_name='Email')
    message= models.TextField(verbose_name='Message') 
    
  
    def __str__(self):
        return f'{self.name}' 
    
    

class Testimonials(models.Model):
    
    class Meta:
        verbose_name_plural='Testimonails'
        verbose_name='Testimonails' 
        ordering=["name"]
        
        
    thumbnail=models.ImageField(blank=True,null=True,upload_to='testimonials')
    name=models.CharField(max_length=200,blank=True,null=True)
    role=models.CharField(max_length=200,blank=True,null=True)
    quote=models.CharField(max_length=200,blank=True,null=True)
    is_active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
  
    
class Media(models.Model):
    
    class Meta:
        verbose_name_plural='Media files'
        verbose_name='Media file' 
        ordering=["name"]
        
        
        
    image=models.ImageField(blank=True,null=True,upload_to="media")
    url=models.URLField(blank=True,null=True)
    name=models.CharField(max_length=200,blank=True,null=True)
    is_image=models.BooleanField(default=True)
        
    def save(self,*args,**kwargs):
        if self.url:
            self.is_image=False
        super(Media,self).save(*args,**kwargs)
        
        
    def __str__(self):
        
            return self.name
        
class Portfolio(models.Model):
    class Meta:
        verbose_name_plural='Portfolio Profiles'
        verbose_name='Portfolio' 
        ordering=["name"]
        
    tech=models.CharField(blank=True,null=True,max_length=50)
    date=models.DateField(blank=True,null=True)
    name=models.CharField(max_length=200,blank=True,null=True)
    description=models.CharField(max_length=500,blank=True,null=True)
    body=RichTextField(blank=True,null=True)
    image=models.ImageField(blank=True,null=True,upload_to='portfolio')
    slug=models.SlugField(blank=True,null=True)
    is_active=models.BooleanField(default=True)
    
    def save(self,*args, **kwargs):
        if not self.id:
            self.slug=slugify(self.name)
        super(Portfolio,self).save(*args,**kwargs)
        
        
        def __str__(self):
            return self.name
        
        def get_absolute_urls(self):
            return f'/portfolio/{self.slug}'
        
        
class Blog(models.Model):   
    class Meta:
        verbose_name_plural='Blog Profiles'
        verbose_name='Blog' 
        ordering=["name"]
        
    timestamp=models.DateField(auto_now_add=True)
    author=models.CharField(max_length=200,blank=True,null=True)
    name=models.CharField(max_length=200,blank=True,null=True)
    description=models.CharField(max_length=500,blank=True,null=True)
    body=RichTextField(blank=True,null=True)
    image=models.ImageField(blank=True,null=True,upload_to='blog')
    slug=models.SlugField(blank=True,null=True)
    is_active=models.BooleanField(default=True)
    
    def save(self,*args, **kwargs):
        if not self.id:
            self.slug=slugify(self.name)
        super(Blog,self).save(*args,**kwargs)
         
        
        def __str__(self):
            return self.name
        
        def get_absolute_urls(self):
            return f'/blog/{self.slug}'
    
    
class Certificate(models.Model):
    class Meta:
        verbose_name_plural='Certificates'
        verbose_name='Certificate'
        
        
    date=models.DateField(blank=True,null=True)
    name=models.CharField(max_length=200,blank=True,null=True)
    title=models.CharField(max_length=200,blank=True,null=True)
    description=models.CharField(max_length=500,blank=True,null=True)
    is_active=models.BooleanField(default=True)

    
            
    def __str__(self):
        return self.name
