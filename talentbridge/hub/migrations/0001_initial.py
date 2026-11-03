from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Job",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=200)),
                ("company", models.CharField(blank=True, max_length=120)),
                ("location", models.CharField(default="Remote", max_length=120)),
                ("description", models.TextField()),
                ("apply_url", models.URLField(help_text="Your referral link")),
                ("active", models.BooleanField(default=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
            options={"ordering": ["-created"]},
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=200)),
                ("slug", models.SlugField(unique=True)),
                ("summary", models.CharField(max_length=300)),
                ("body", models.TextField()),
                ("published", models.BooleanField(default=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
            options={"ordering": ["-created"]},
        ),
        migrations.CreateModel(
            name="Lead",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("kind", models.CharField(max_length=20)),
                ("name", models.CharField(max_length=120)),
                ("email", models.EmailField(max_length=254)),
                ("company", models.CharField(blank=True, max_length=120)),
                ("service", models.CharField(blank=True, choices=[
                    ("Web development", "Web development"), ("Mobile app", "Mobile app"),
                    ("Custom software", "Custom software"), ("AI automation / chatbots", "AI automation / chatbots"),
                    ("API integration", "API integration"), ("Hiring developers", "Hiring developers"),
                    ("Other", "Other")], max_length=60)),
                ("budget", models.CharField(blank=True, choices=[
                    ("Under $1,000", "Under $1,000"), ("$1,000 - $5,000", "$1,000 - $5,000"),
                    ("$5,000 - $20,000", "$5,000 - $20,000"), ("Over $20,000", "Over $20,000"),
                    ("Not sure yet", "Not sure yet")], max_length=40)),
                ("message", models.TextField()),
                ("created", models.DateTimeField(auto_now_add=True)),
            ],
            options={"ordering": ["-created"]},
        ),
    ]
