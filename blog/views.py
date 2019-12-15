from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from blog.models import Post


def post_list(request):
    # cur_file_path = os.path.abspath(__file__)
    # blog_file_path = os.path.dirname(cur_file_path)
    # root_file_path = os.path.dirname(blog_file_path)
    #
    # templates_file_path = os.path.join(root_file_path, 'templates')
    # post_list_html_path = os.path.join(templates_file_path, 'post-list.html')
    #
    # f = open(post_list_html_path, 'rt')
    # html = f.read()
    # f.close()

    # return HttpResponse(html)

    # content = loader.render_to_string('post-list.html', None, request)
    # return HttpResponse(content)

    # posts = Post.objects.all()
    posts = Post.objects.order_by('-pk')

    context = {
        'posts': posts,
    }

    return render(request, 'post-list.html', context)


def post_detail(request, pk):
    # posts = Post.objects.filter(pk=pk)
    # post = posts[0]

    # try:
    #     posts = Post.objects.filter(pk=pk)
    #     post = posts[0]
    # except:
    #     return HttpResponse('없음')

    post = get_object_or_404(Post, pk=pk)

    context = {
        'post': post,
    }

    return render(request, 'post-detail.html', context)


def post_add(request):
    if request.method == 'POST':
        print('request', request)
        author = request.user
        title = request.POST['title']
        text = request.POST['text']

        post = Post.objects.create(
            title=title,
            author=author,
            text=text,
        )

        print('post',post)
        # result = f'title: {post.title}, created_date: {post.created_date}'
        # return HttpResponse(result)
        return redirect('post-list')

    else:
        return render(request, 'post-add.html')