from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render, redirect
from .forms import CreateNewTask, CreateNewProject

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
	return render(request, 'projects/projects.html', {
		'projects': projects
	})

def tasks(request):
	# task = Task.objects.get(pk=id) # consulta normal	
	#task = get_object_or_404(Task, id=id)
	#return HttpResponse("task: %s" % task.title)
	tasks = Task.objects.all()
	return render(request, 'tasks/tasks.html', {
		'tasks': tasks
	})

def create_task(request):
	if request.method == 'GET':
		return render(request, 'tasks/create_task.html', {
			'form': CreateNewTask()
		})
	else:
		Task.objects.create(title=request.POST['title'], 
			description=request.POST['description'], project_id=1)
		return redirect('tasks')

def create_project(request):
	if request.method == 'GET':
		return render(request, 'projects/create_project.html', {
			'form': CreateNewProject()
		})
	else:
		Project.objects.create(name=request.POST['name'])
		return redirect('projects')

def project_detail(request, id):
	#project = Project.objects.get(id=id)
	project = get_object_or_404(Project, id=id)
	tasks = Task.objects.filter(project_id=id)
	return render(request, 'projects/detail.html', {
		'project': project,
		'tasks': tasks
	})
