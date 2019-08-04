from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .forms import NameForm
from django.http import HttpResponseRedirect
from django.template import loader
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required

# Create your views here.





def index(request):
    if request.POST:
        new_post_input = {
            "post_title": request.POST.get("post_title"),
            "post_content": request.POST.get("post_content"),
            "post_author": request.POST.get("post_author"),
            "pub_date": request.POST.get("pub_date")
        }
        new_post = Post.objects.create(**new_post_input)
        return HttpResponseRedirect("index")
    else:
        Post_template = Post.objects.order_by('-pub_date')[:]
        context = {'Post_template': Post_template}
        return render(request, 'bilboard/index.html', context)

# def add_new_post(request):
#     if request.POST:
#         new_post_input = {
#             "post_title": request.POST.get("post_title"),
#             "post_content": request.POST.get("post_content"),
#             "post_author": request.POST.get("post_author"),
#             "pub_date": request.POST.get("pub_date")
#         }
#         new_post = Post.objects.create(**new_post_input)
#         return HttpResponseRedirect("bilboard/index.html")
#     else:
#         return render(request, "SocialBoard/board.html")
