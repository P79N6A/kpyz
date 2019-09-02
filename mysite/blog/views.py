from django.shortcuts import render_to_response,get_object_or_404
from .models import Blog,BlogType

# Create your views here.
def blog_list(request):
    context = {}
    context['blogs'] = Blog.objects.all()
    return render_to_response('blog_list.html',context)

def blog_detail(request,blog_pk):
    context = {}
    context['blog'] = get_object_or_404(Blog,pk = blog_pk)
    return render_to_response('blog_detail.html',context)

def blog_type(request,blogs_with_type):
    context = {}
    blog_type = get_object_or_404(BlogType,pk = blogs_with_type)
    context['blogs'] = Blog.objects.filter(type = blog_type)
    context['blog_type'] = blog_type
    return render_to_response('blogs_with_type.html',context)

def home(request):
    return render_to_response('home.html')

def about(request):
    return render_to_response('about.html')

def asso_list(request):
    return render_to_response('asso_list.html')

def test(request):
    return render_to_response('test.html')