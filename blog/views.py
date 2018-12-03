from msilib.schema import ListView

from blog.forms import CommentForm, PostForm, ContactForm,SignUpForm
from blog.serializers import PostSerializer
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.http import *
from blog.models import Post, Comments
from business.models import Add
# Create your views here.
from django.urls import reverse
from django.views.generic import TemplateView,ListView,DetailView
from mydjango.settings import DEFAULT_FROM_EMAIL
from rest_framework import status
from rest_framework.renderers import JSONRenderer


def index(request):
    he={'sujan':[1,2,3,4,5,6,7,8,9,10]}
    return render(request,template_name='index.html',context=he)





def home(request):
    #object_list=Post.objects.order_by('-created_date')
    #count=object_list.count()
    #ct={
    #     "object_list":object_list,"count":count
    # }
    return render(request,template_name='home.html',context={})

def about(request):
    return render(request,template_name='about.html',context={})

def contact(request):
    form = ContactForm(request.POST)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("http://127.0.0.1:8000/home/")
    else:
        return render(request, 'contact.html', {"form":form})




def get_one_post(request,*args,**kwargs):
    p=kwargs.get('pop')
    one_post=get_object_or_404(Post,pk=p)

    ctx={"one_post":one_post
    }
    return render(request,'post_detail.html',context=ctx)

class HomeView(TemplateView):
    def get(self,request,*args,**kwargs):
        object_list = Post.objects.order_by('-created_date')
        count = object_list.count()
        ct = {
            "object_list": object_list, "count": count
        }
        return render(request, template_name='home.html', context=ct)

# class ContactView(TemplateView):
#     def get(self,request,*args,**kwargs):
#         return render(request, template_name='contact.html', context={})


class PostListView(ListView):
    model = Post
    context_object_name = "posts_list"
    #queryset = Post.objects.order_by('-created')
    #Option 2
    # def get_queryset(self):
    #     return Post.objects.order_by('-created_date')

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        # context['object_list'] = Post.objects.order_by('-created')
        #context['posts_list'] = Post.objects.filter(status='published').order_by('-created')
        context['posts_list'] = Post.published.all()

        #context['count'] = context['object_list'].count()
        return context

    template_name='blog/home.html'

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'one_post'
    template_name = 'blog/post_detail.html'

    def get(self,request,*args,**kwargs):
        p = kwargs.get('pk')
        try:
            one_post = Post.objects.get(
                Q(pk=p) & Q(status='published'))
        except:
            raise Http404
        #comments=Comments.objects.filter(post_id=one_post)
        comments=one_post.post_comments.all()

        #prepare Form
        comment_form=CommentForm()

        ctx = {"one_post": one_post,
               'comments':comments,
               "comment_form":comment_form
                   }
        return render(request, 'blog/post_detail.html', context=ctx)


    def post(self,request,*args,**kwargs):
        comments=CommentForm(data=request.POST)
        if comments.is_valid():
            new_comment=comments.save(commit=False)
            post_comment=get_object_or_404(Post,pk=kwargs.get('pk'))
            new_comment.post_id=post_comment
            new_comment.save()
            return redirect('blog:detail',pk=post_comment.pk)
    # def get_context_data(self, **kwargs):
    #     context=super(PostDetailView,self).get_context_data(**kwargs)
    #     context['comment']=Comments.objects.all()
    #     return context
@login_required
def post(request):
    if request.method=='POST':
        com = PostForm(request.POST,request.FILES)
        if com.is_valid():
            post=com.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('blog:home')
    else:
        post_list = PostForm()
        ctx = {'post_list': post_list

               }
    return render(request,template_name='post.html',context=ctx)


def search(request,*args,**kwargs):
    query=request.POST.get('searchquery')
    data=Post.objects.filter(Q(title__contains=query) | Q(body__contains=query)).filter(status='published')
    count=data.count()
    ctx={
        'result':data,'count':count
    }
    return render(request,'blog/searchresult.html',context=ctx)
@login_required
def register(request):
    if request.method=='POST':
        user_form=UserCreationForm(data=request.POST)
        if user_form.is_valid():
            new_user=user_form.save()
            return redirect('blog:login')
    else:
        form=UserCreationForm()
    return render(request,'blog/register.html',{'form':form})

class JSONResponse(HttpResponse):
    def __init__(self,data,*args,**kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type']='application/json'
        super(JSONResponse,self).__init__(content,**kwargs)

def post_list_api(request):
    if request.method == 'GET':
        posts = Post.published.all()
        post_serializer= PostSerializer(posts,many=True)
        return JSONResponse(post_serializer.data)

def post_detail_api(request,pk):
    try:
        one_post=Post.published.get(pk=pk)
    except Post.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        post_detail_serializer=PostSerializer(one_post)
        return JSONResponse(post_detail_serializer.data)


def api_doc(request):
    return render(request,template_name='blog/api_doc.html')



from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('blog:home')
    else:
        form = SignUpForm()
    return render(request,'blog/signup.html', {'form': form})











def delete(request,pk,author,aut):
    if author==aut:
        Post.objects.filter(pk=pk).delete()
        return HttpResponseRedirect("http://127.0.0.1:8000/home/")
    else:
        return HttpResponseRedirect("http://127.0.0.1:8000/home/")


def GetAdd(request):
    value=Add.objects.all()
    return render(request,"index.html",{'value':value})


class AddDetailView(DetailView):
    model = Add
    context_object_name = 'one_post'
    template_name = 'blog/add_detail.html'

    def get(self,request,*args,**kwargs):
        p = kwargs.get('pk')
        try:
            one_post = Add.objects.get(pk=p)
        except:
            raise Http404
        #comments=Comments.objects.filter(post_id=one_post)


        #prepare Form


        ctx = {"one_post": one_post,
                   }
        return render(request, 'blog/add_detail.html', context=ctx)
