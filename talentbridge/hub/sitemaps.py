from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Job, Post


class Static(Sitemap):
    def items(self):
        return ["home", "jobs", "blog", "companies", "developers", "about", "contact"]

    def location(self, item):
        return reverse(item)


class Jobs(Sitemap):
    def items(self):
        return Job.objects.filter(active=True)


class Posts(Sitemap):
    def items(self):
        return Post.objects.filter(published=True)


SITEMAPS = {"static": Static, "jobs": Jobs, "posts": Posts}
