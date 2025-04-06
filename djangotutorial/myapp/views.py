from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render

# Create your views here.
def index(request):
	title = 'Welcome to Django page!!'
	return render(request, 'index.html', {
		'title': title
	})

def hello(request, username):
	return HttpResponse('<h2>Hello %s<h2>' % username)

def about(request):
	username = 'mint'
	return render(request, 'about.html', {
		'username': username
	})

def projects(request):
	#projects = list(Project.objects.values())
	projects = Project.objects.all() 
	#return JsonResponse(projects, safe=False)
	return render(request, 'projects.html', {
		'projects': projects
	})

def tasks(request):
	# task = Task.objects.get(pk=id) # consulta normal	
	#task = get_object_or_404(Task, id=id)
	#return HttpResponse("task: %s" % task.title)
	tasks = Task.objects.all()
	return render(request, 'tasks.html', {
		'tasks': tasks
	})