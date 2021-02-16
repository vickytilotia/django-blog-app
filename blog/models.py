from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):

    class NewManager(models.Manager):
        # This will allow to choose only published blogs
        # This will be used in blog.views
        def get_queryset(self):
            return super().get_queryset().filter(status='published')
    


    options = (
        ('draft','Draft'),
        ('published','Published'),
    )

    title = models.CharField(max_length= 250)
    slug = models.SlugField(max_length= 250, unique_for_date='publish')
    publish = models.DateTimeField(default = timezone.now)
    author = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'blog_posts')
    content = models.TextField()
    status = models.CharField(max_length=10, choices=options, default= 'draft')
    objects = models.Manager()  #This one is the default manager
    newmanager = NewManager()   #This one is the custom created manager

    class Meta:
        # order of blog posts in admin area
        # use -publish instead of publish , to reverse the order
        ordering = ('publish',)

    def __str__(self):
        # responsible to show name of blog in admin instead of object1
        # also look the authoradmin class in admin.py 
        return self.title

    def get_absolute_url(self):
        return reverse("blog:post_single", args=[self.slug])
        
    
    
