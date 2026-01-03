from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.urls import path


def index(request):
    """Главная страница."""
    from subscriptions.models import Plan
    from blog.models import BlogPost
    
    plans = Plan.objects.filter(is_active=True).order_by("price")
    
    latest_posts = BlogPost.objects.filter(
        status=BlogPost.Status.PUBLISHED
    ).select_related("category").order_by("-published_at")[:3]
    
    return render(request, "pages/index.html", {
        "plans": plans,
        "latest_posts": latest_posts,
    })


def cookies(request):
    """Cookie-Einstellungen."""
    return render(request, "pages/cookies.html")