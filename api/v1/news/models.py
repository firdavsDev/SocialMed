from django.db import models
#ckeditor
from ckeditor.fields import RichTextField


# News article model
class News(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='news/', null=True, blank=True)
    views_count = models.IntegerField(default=0)
    class Meta:
        db_table = 'news'
        ordering = ['-created_at']
        verbose_name = 'New'
        verbose_name_plural = 'News'
        
    def __str__(self):
        return self.title
    
    