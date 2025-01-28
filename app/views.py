from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import BlogForm
from .models import blog
# Create your views here.
def index(request):
    blogs = blog.objects.all()
    return render(request,'index.html',{'blogs':blogs})

def addblog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request,'addblog.html',{'form':form})
    else:
        form = BlogForm()
        return render(request,'addblog.html',{'form':form})