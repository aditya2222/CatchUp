from django.shortcuts import render,redirect
from .forms import SignUpForm,CreatePostForm
from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse_lazy
from .models import Post
# Create your views here.

class CreateUserView(CreateView):
	form_class = SignUpForm
	success_url = reverse_lazy('login')
	template_name = 'app/signup.html'


def create_post(request):
	form = CreatePostForm(request.POST or None)
	context = {
	"form":form
	}
	if form.is_valid():
		title = form.cleaned_data['Title']
		description = form.cleaned_data['Description']
		CurrentUser = request.user
		Post.objects.create(Title=title,Description=description,CurrentUser=CurrentUser)
		return redirect("home")

	return render(request,'app/createpost.html',context)





class HomeView(ListView):
	model = Post
	template_name = 'app/index.html'
	paginate_by = 10
	def get_queryset(self):
		return Post.objects.all()

class MyPostsView(ListView):
	model=Post
	template_name = 'app/index.html'
	paginate_by = 10
	def get_queryset(self):
		return Post.objects.filter(CurrentUser=self.request.user)



class PostDetailView(DetailView):
	template_name ='app/details.html'
	model = Post