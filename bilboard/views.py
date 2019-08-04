from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .forms import NameForm
from django.http import HttpResponseRedirect
from django.template import loader
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import   authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

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


# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'signup.html', {'form': form})