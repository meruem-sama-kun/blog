from django.shortcuts import render

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Post


from django.views.generic import ListView, DetailView

from django.urls import reverse_lazy

from .models import Post

context_object_name = 'all_post_list'

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'indiv_post'

class BlogCreateView(ListView): # new
    model = Post
    template_name = 'post_new.html'

class BlogDetailView(ListView):
    model = Post
    template_name = 'home.html'
    fields = '__all__'

class BlogUpdateView(UpdateView): # new
        model = Post
        template_name = 'post_edit.html'
        fields = ['title', 'body']

class BlogDeleteView(DeleteView): # new
        model = Post
        template_name = 'post_delete.html'
        success_url = reverse_lazy('home')