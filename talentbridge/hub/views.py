from django.forms import modelform_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.http import url_has_allowed_host_and_scheme

from .i18n import LANGS, tr
from .models import Job, Lead, Post


def home(r):
    return render(r, "hub/home.html", {
        "jobs": Job.objects.filter(active=True)[:3],
        "posts": Post.objects.filter(published=True)[:3],
    })


def jobs(r):
    return render(r, "hub/jobs.html", {"jobs": Job.objects.filter(active=True)})


def job(r, pk):
    return render(r, "hub/job.html", {"job": get_object_or_404(Job, pk=pk, active=True)})


def blog(r):
    return render(r, "hub/blog.html", {"posts": Post.objects.filter(published=True)})


def post(r, slug):
    return render(r, "hub/post.html", {"post": get_object_or_404(Post, slug=slug, published=True)})


def about(r):
    return render(r, "hub/about.html")


def lead_view(kind, title_key, sub_key, fields):
    Form = modelform_factory(Lead, fields=fields)

    def view(r):
        form = Form(r.POST or None)
        for name, field in form.fields.items():
            field.label = tr(r, name)
        if r.method == "POST" and form.is_valid():
            lead = form.save(commit=False)
            lead.kind = kind
            lead.save()
            return redirect(f"{r.path}?sent=1")
        return render(r, "hub/lead.html", {
            "form": form, "title": tr(r, title_key), "sub": tr(r, sub_key), "sent": r.GET.get("sent"),
        })
    return view


def set_lang(r, code):
    if code in LANGS:
        r.session["lang"] = code
    nxt = r.GET.get("next", "/")
    if not url_has_allowed_host_and_scheme(nxt, allowed_hosts={r.get_host()}):
        nxt = "/"
    return redirect(nxt)
