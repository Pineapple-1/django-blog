from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView ,  UpdateView
from .models import post
# Create your views here.

class PostListView(ListView):
    model = post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = post

class PostCreateView(CreateView):
    model = post
    fields = ['title','content']
    
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    



def about(request):
    return render(request, 'blog/about.html', {'pageTitle': 'about'})
