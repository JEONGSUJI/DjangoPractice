import os

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


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

    return render(request, 'post-list.html')