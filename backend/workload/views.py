from django.http import JsonResponse
from .models import Task

# Create your views here.
def task_list(request):
    tasks = Task.objects.all().values('id', 'title', 'description', 'completed')
    tasks_list = list(tasks)
    return JsonResponse(tasks_list, safe=False)
