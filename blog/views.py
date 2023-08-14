from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def blog_view(request, **kwargs):
    posts = Post.objects.filter(published_date__lte=timezone.now()).filter(status=1)
    if kwargs.get('cat_name') != None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') != None:
        posts = posts.filter(author__username=kwargs['author_username'])
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])

    posts = Paginator(posts, 2)
    page_range = posts.page_range
    page = request.GET.get('page')
    try:
        posts = posts.page(page)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)

    context = {'posts':posts, 'page_range':page_range}
    return render(request, 'blog/blog-home.html', context=context)


def single_view(request, pid):
    #posts = Post.objects.filter(status=1)
    #post = get_object_or_404(posts, pk=pid)
    post = get_object_or_404(Post, pk=pid, status=1)
    post.counted_view += 1
    post.save()

    next_post=False
    prev_post=False
    for i in range(len(Post.objects.all())-pid):
        if(Post.objects.filter(pk=pid+i+1).filter(status=1).exists()):
            next_post = get_object_or_404(Post, pk=pid+i+1) #it exists for sure since it should pass the .exists() filter. anyway...
            break
        else:
            next_post=False

    for i in range(pid):
        if(Post.objects.filter(pk=pid-i-1).filter(status=1).exists()):
            prev_post = get_object_or_404(Post, pk=pid-i-1) #it exists for sure since it should pass the .exists() filter. anyway...
            break

    context = {'post':post, 'next_post': next_post, 'prev_post': prev_post}
    return render(request, 'blog/blog-single.html', context=context)



def blog_category(request, cat_name):
    posts = Post.objects.filter(status=1).filter(category__name=cat_name)
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html', context=context)

#def test(request, pid):
    post = get_object_or_404(Post, pk=pid)
    context = {'post':post}
    return render(request, 'test.html', context=context)

def test(request):
    return render(request, 'test.html')


def blog_search(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).filter(status=1)

    if(request.method=='GET'):
        if s:= request.GET.get('s'):
            posts = posts.filter(content__contains=s)

    context = {'posts':posts}
    return render(request, 'blog/blog-home.html', context=context)