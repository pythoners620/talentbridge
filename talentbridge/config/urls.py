from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.http import HttpResponse
from django.urls import path, include
from hub.sitemaps import SITEMAPS

urlpatterns = [
    path("admin/", admin.site.urls),
    path("sitemap.xml", sitemap, {"sitemaps": SITEMAPS}),
    path("robots.txt", lambda r: HttpResponse(f"User-agent: *\nAllow: /\nSitemap: {r.build_absolute_uri('/sitemap.xml')}\n", content_type="text/plain")),
    path("", include("hub.urls")),
]
