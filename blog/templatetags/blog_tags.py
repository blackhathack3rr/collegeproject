from django import template
from django.db.models import Q
from mydjango.settings import BLOG_NAME
from blog.models import Post
from _datetime import datetime
from mydjango.settings import BLOG_NAME
register=template.Library()

#1. Simple Tag
@register.simple_tag()
def blog_name():
    return BLOG_NAME

@register.simple_tag()
def count():
    return Post.published.all().count()

@register.simple_tag()
def footer():
    return "Copyright@"+ str(datetime.today().date())


#2. Inclusion Tag
@register.inclusion_tag('blog/latest.html')
def get_latest(count=None):
    latest=[]
    if count is not None:
        latest= Post.published.all()[:count]
    else:
        latest=Post.published.all()[:4]
    return {'latest_blogs':latest}


#3. Assignment
@register.assignment_tag
def similar(title,q_pk):
    similars=Post.published.filter(
        Q(title__contains=title)|Q(body__contains=title)).exclude(pk=q_pk)
    return similars

#4. Custom Filters
@register.filter()
def capitalize(title):
    return title.upper()

