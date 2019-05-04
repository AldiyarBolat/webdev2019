
from api.models import TaskList, Task
from api.serializers import TaskListSerializer, TaskListSerializer2, TaskSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


@api_view(['GET', 'POST'])
def task_lists(request):   # List of all TaskList
    if request.method == 'GET':
        taskLists = TaskList.objects.all()
        serializer = TaskListSerializer(taskLists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':    # Create TaskList
        serializer = TaskListSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PUT', 'DELETE'])
def task_list(request, pk):  # Get TaskList
   try:
       taski = TaskList.objects.get(id=pk)
   except  TaskList.DoesNotExist as e:
       return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)

   if request.method == 'GET':
       serializer = TaskListSerializer(taski)   # Get TaskList
       return Response(serializer.data, status=status.HTTP_200_OK)
   elif request.method == 'PUT':
       serializer = TaskListSerializer(instance=taski, data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_200_OK)
       return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
   elif request.method == 'DELETE':
       taski.delete()
       return Response({}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def task_lists_tasks(request, pk):   # all tasks for tasklist with id
    try:
        list = TaskList.objects.get(id=pk)
    except TaskList.DoesNotExist as e:
        return Response({'error': str(e)}, status=status.HTTP_404_NOT_FOUND)
    tasks = list.task_set.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def tasks(request):
    if request.method == 'GET':  # List of all Tasks
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':  # Create Task
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class TaskView(APIView):

    def get_object(self, pk):
        try:
           return Task.objects.get(id=pk)
        except  Task.DoesNotExist:
           raise Http404


    def get(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskListSerializer(instance=task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def delete(self, request, pk):
        task = self.get_object(pk)
        task.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)



# GENERIC VIEW

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, )

@api_view(['POST'])
def login(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer .validated_data.get('user')
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key})

@api_view(['POST'])
def logout(request):
    request.auth.delete()
    return Response(status=status.HTTP_200_OK)

