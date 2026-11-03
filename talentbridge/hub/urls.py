from django.urls import path
from . import views as v

urlpatterns = [
    path("", v.home, name="home"),
    path("jobs/", v.jobs, name="jobs"),
    path("jobs/<int:pk>/", v.job, name="job"),
    path("blog/", v.blog, name="blog"),
    path("blog/<slug:slug>/", v.post, name="post"),
    path("for-companies/", v.lead_view("company", "companies_title", "companies_sub", ["name", "email", "company", "service", "budget", "message"]), name="companies"),
    path("for-developers/", v.lead_view("developer", "developers_title", "developers_sub", ["name", "email", "message"]), name="developers"),
    path("contact/", v.lead_view("contact", "contact_title", "contact_sub", ["name", "email", "message"]), name="contact"),
    path("about/", v.about, name="about"),
    path("lang/<str:code>/", v.set_lang, name="set_lang"),
]
