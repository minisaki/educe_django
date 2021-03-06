from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from .fileds import OrderFiled
from django.template.loader import render_to_string
# Create your models here.


class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Course(models.Model):
    owner = models.ForeignKey(User, related_name='courses_created',
                              on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name='courses',
                                on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    students = models.ManyToManyField(User, related_name='courses_joined',
                                      blank=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


class Module(models.Model):
    course = models.ForeignKey(Course, related_name='modules',
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order = OrderFiled(blank=True, for_fields=['course'])

    def __str__(self):
        return "{}.{}".format(self.order, self.title)

    class Meta:
        ordering = ['order']


class Content(models.Model):
    module = models.ForeignKey(Module, related_name='contents',
                               on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,
                                     limit_choices_to={'model__in': ('text',
                                     'video', 'image', 'file')})
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')
    order = OrderFiled(blank=True, for_fields=['module'])

    class Meta:
        ordering = ['order']


class ItamBase(models.Model):
    owner = models.ForeignKey(User, related_name='%(class)s_related',
                              on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def render(self):
        return render_to_string('courses/content/{}.html'.format(self._meta.model_name), {'item': self})

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Text(ItamBase):
    content = models.TextField()


class File(ItamBase):
    file = models.FileField(upload_to='files')


class Image(ItamBase):
    file = models.ImageField(upload_to='images')


class Video(ItamBase):
    url = models.URLField()
