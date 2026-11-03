from django.db import models
from django.urls import reverse


class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=120, blank=True)
    location = models.CharField(max_length=120, default="Remote")
    description = models.TextField()
    apply_url = models.URLField(help_text="Your referral link")
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("job", args=[self.pk])


class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    summary = models.CharField(max_length=300)
    body = models.TextField()
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post", args=[self.slug])


def _c(*items):
    return [(i, i) for i in items]


class Lead(models.Model):
    SERVICES = _c("Web development", "Mobile app", "Custom software", "AI automation / chatbots",
                  "API integration", "Hiring developers", "Other")
    BUDGETS = _c("Under $1,000", "$1,000 - $5,000", "$5,000 - $20,000", "Over $20,000", "Not sure yet")
    kind = models.CharField(max_length=20)  # company / developer / contact
    name = models.CharField(max_length=120)
    email = models.EmailField()
    company = models.CharField(max_length=120, blank=True)
    service = models.CharField(max_length=60, blank=True, choices=SERVICES)
    budget = models.CharField(max_length=40, blank=True, choices=BUDGETS)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"{self.kind}: {self.name}"
