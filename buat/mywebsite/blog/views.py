from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'judul ' : 'coba',
        'sub judul' : 'blog'

    }
    return render(request,'blog/index.html',context)