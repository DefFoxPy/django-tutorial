from django.http import HttpResponse, JsonResponse
from .models import Project, Task

# Create your views here.
def index(request):
	return HttpResponse("Index page")

def hello(request, username):
	return HttpResponse('<h2>Hello %s<h2>' % username)

def about(request):
	return HttpResponse("About")

def projects(request):
	projects = list(Project.objects.values())
	return JsonResponse(projects, safe=False)

def tasks(request):
	return HttpResponse("tasks")