from django.db import models


# Create your models here.
from django.urls import reverse
from django.utils.text import slugify


class Tags(models.Model):
    name = models.TextField(max_length=30)
    color = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Post(models.Model):
    image = models.TextField(max_length=1000, default=None)
    # image = models.FileField(upload_to='images/', default=None)
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=300, default='', editable=False)

    created = models.DateTimeField(auto_now_add=True)
    published_date = models.DateField()

    body = models.TextField(max_length=10000, default=None)
    tags = models.ManyToManyField(Tags)

    claps = models.IntegerField(default=0)

    published = models.BooleanField(default=False)
    drafted = models.BooleanField(default=True)

    class Meta:
        ordering = ['-published_date']

    def __str__(self):
        return '%s :-: %s' % (self.title, self.published_date)

    def get_absolute_url(self):
        kwargs = {
            # 'pk': self.id,
            'slug': self.slug,
        }
        return reverse('blog-detail', kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)

        super().save(*args, **kwargs)
