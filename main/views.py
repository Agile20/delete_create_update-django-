from django.shortcuts import render, get_object_or_404, redirect
from main.models import Post, Comment
from main.forms import PostForm
def index(request):
    posts = Post.objects.all()
    template_name ='index.html'
    context = {
        'posts': posts
    }
    return render(request, template_name, context)


def detail_post(request,post_id):
    template_name = 'detail_post.html'
    post = get_object_or_404(Post, id =post_id)
    context = {
        'post': post,
    }
    return render(request, template_name, context)
def create_post(request):
    template_name = 'create_post.html'
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PostForm()
    return render(request, template_name, {'form': form})
def update_post(request,post_id):
    template_name = 'update_post.html'
    post = get_object_or_404(Post, id = post_id)
    form =PostForm(request.POST or None, instance = post)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, template_name, {'form': form, 'post':post})

def delete_post(request,post_id):
    post = get_object_or_404(Post, id = post_id)
    post.delete()
    return redirect('/')