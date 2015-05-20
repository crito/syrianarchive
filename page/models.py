from django.db import models
from django.contrib.auth.models import User
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class Page(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField(max_length=50000, null=True, blank=True)
    linked_pages = models.ManyToManyField("self", null=True, blank=True)
    url = models.SlugField(max_length=250)

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Page, self).save(*args, **kwargs)

class Post(Page):
    main_image = models.ImageField(null=True,blank=True, upload_to="blog_images")
    short_description = models.TextField(max_length=500, null=True, blank=True)
    pass

