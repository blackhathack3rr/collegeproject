from django.conf.urls import url, include
from blog import views
from django.contrib.auth.views import PasswordChangeView
from django.views.generic import TemplateView

app_name='blog'
urlpatterns=[
    url(r'^home/',views.GetAdd,name="index"),
    url(r'^post/',views.post,name='post'),
    url(r'^register/',views.register,name='register'),
    url(r'^delete/(?P<pk>[0-9]+)/(?P<author>\D+)//(?P<aut>\D+)/$',views.delete,name='delete'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^accounts/',include("django.contrib.auth.urls"), name='accounts'),
#    url(r'^password_change/$',PasswordChangeView.as_view(),name='password_change'),
    #url(r'^changed/',views.contact,name='password_change_done'),
    url(r'^search/',views.search,name='search'),
    url(r'^apis/', views.api_doc, name='api_doc'),
    url(r'^api/posts/$',views.post_list_api,name='list_api_view'),
    url(r'^api/post/(?P<pk>[0-9]+)/$',views.post_detail_api,name='detail_api_view'),
    #url(r'^home/', views.home),
    #url(r'^home/', views.HomeView.as_view(),name="home"),
    url(r'^$', views.PostListView.as_view(),name="home"),
    url(r'^post_detail/(?P<pk>\d+)', views.PostDetailView.as_view(), name='detail'),
    url(r'^add_detail/(?P<pk>\d+)', views.AddDetailView.as_view(), name='adddetail'),
    #url(r'^about/', views.about),
    url(r'^about/', TemplateView.as_view(template_name='about.html'),name='about'),
    url(r'^contact/', views.contact,name="contact"),
    #url(r'^contact/',views.contact)
    url(r'^apii/',include("blog.api.urls",namespace='blogapi')),
]