import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api.models import TaskList
from api.serializers import TaskListSerializer, TaskListSerializer2, TaskSerializer


@csrf_exempt
def task_lists(request):   #List of all TaskList
    if request.method == 'GET':
        categories = TaskList.objects.all()
        serializer = TaskListSerializer(categories, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)

    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = TaskListSerializer2(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors)


@csrf_exempt
def get_task_list(request, pk):  #Get one TaskList
   try:
       taski = TaskList.objects.get(id=pk)
   except  TaskList.DoesNotExist as e:
       return JsonResponse({'error': str(e)})

   if request.method == 'GET':
       serializer = TaskListSerializer(taski)
       return JsonResponse(serializer.data, status=200)
   elif request.method == 'PUT':
       data = json.loads(request.body.decode('utf-8'))
       serializer = TaskListSerializer(instance=taski, data=data)
       if serializer.is_valid():
           serializer.save()  # update function in serializer class
           return JsonResponse(serializer.data, status=200)
       return JsonResponse(serializer.errors)
   elif request.method == 'DELETE':
       taski.delete()
       return JsonResponse({}, status=204)


@csrf_exempt
def task_lists_tasks(request, pk):   # all tasks for tasklist with id
    try:
        list = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    tasks = list.task_set.all()
    serializer = TaskSerializer(tasks, many=True)
    return JsonResponse(serializer.data, safe=False)