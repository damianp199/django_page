from django.shortcuts import render
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView
	)
from .models import Post
from django.urls import reverse



def home(request):
	
	form = Post(request.POST or None, request.FILES or None)
	if form.is_valid():
		form.save()

	context = {
	'posts': Post.objects.all(),
	'form': form
	}
	return render(request, 'page/home.html', context)

class PostListView(ListView):
	model = Post
	template_name = 'page/home.html'
	context_object_name = 'posts'
	ordering =['-date_posted']

class PostDetailView(DetailView):
	model = Post
	template_name = 'page/single_post.html'

class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	template_name = 'page/post_form.html'
	fields = ['title', 'content', 'video']
	success_url = '/'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	template_name = 'page/post_form.html'
	fields = ['title', 'content', 'video']
	success_url = '/'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	template_name = 'page/post_confirm_delete.html'
	success_url = '/'


	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

def about(request):
	return render(request, 'page/about.html', {'title': 'About'})

# Create your views here.
