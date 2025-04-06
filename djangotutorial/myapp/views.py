from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render

# Create your views here.
def index(request):
	return render(request, 'index.html')

def hello(request, username):
	return HttpResponse('<h2>Hello %s<h2>' % username)

def about(request):
	return render(request, 'about.html')

def projects(request):
	projects = list(Project.objects.values())
	#return JsonResponse(projects, safe=False)
	return render(request, 'projects.html')

def tasks(request):
	# task = Task.objects.get(pk=id) # consulta normal
	#task = get_object_or_404(Task, id=id)
	#return HttpResponse("task: %s" % task.title)
	return render(request, 'tasks.html')