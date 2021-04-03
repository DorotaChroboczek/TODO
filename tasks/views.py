from django.shortcuts import redirect, render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import TaskSerializer, MembersGroupSerializer
from .models import Task
from .forms import *


@api_view(['GET'])
def index(request):
    api_urls = {
        'List': '/task-list/',
        'Detail View': '/task-detail/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def task_list(request):
    tasks = Task.objects.all().order_by('-id')
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def task_detail(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def task_create(request):
    serializer = TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['GET', 'POST'])
def task_update(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task,
                                data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def task_delete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response('Item successfully deleted!')


@api_view(['GET'])
def member_list(request):
    members = MembersGroup.objects.all()
    serializer = MembersGroupSerializer(members, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def member_detail(request, pk):
    members = MembersGroup.objects.get(id=pk)
    serializer = MembersGroupSerializer(members, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def member_create(request):
    serializer = MembersGroupSerializer(data=request.data)

    if serializer.is_valid():
        serializer.person = request.person
        serializer.save()

    return Response(serializer.data)


@api_view(['GET', 'POST'])
def member_update(request, pk):
    member = MembersGroup.objects.get(id=pk)
    serializer = MembersGroupSerializer(instance=member,
                                        data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def member_delete(request, pk):
    member = MembersGroup.objects.get(id=pk)
    member.delete()
    return Response('Item successfully deleted!')


# def index(request):
#     members = MembersGroup.objects.filter(person=request.user.profile)
#     tasks = Task.objects.get(person=request.user.profile)
#
#     form = TaskForm()
#
#     if request.method == 'POST':
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             new_task = form.save(commit=False)
#             new_task.member = request.member
#             new_task.title = request.title
#             new_task.save()
#             context = {}
#             context['new_task'] = new_task
#         return redirect('/')
#
#     context = {'tasks': tasks, 'members': members, 'form': form}
#     return render(request, 'tasks.html', context)


