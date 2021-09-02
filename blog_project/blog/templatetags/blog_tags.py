from django import template
from blog.models import Post
from django.db.models import Count
register = template.Library()

@register.simple_tag
def total_posts():
    return Post.objects.count()

@register.inclusion_tag('blog/latest_posts.html')
def latest_posts(count=3):
    latest_posts = Post.objects.all().order_by('-publish')[:count]
    return {'latest_posts':latest_posts}

@register.inclusion_tag('blog/most_commented.html')
def most_commented_posts(count=3):
    most_commented = Post.objects.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]
    return{'most_commented':most_commented}