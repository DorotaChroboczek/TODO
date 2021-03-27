from django.shortcuts import redirect, render

from .forms import *


def index(request):
    members = MembersGroup.objects.filter(person=request.user.profile)
    tasks = Task.objects.get(person=request.user.profile)

    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.member = request.member
            new_task.title = request.title
            new_task.save()
            context = {}
            context['new_task'] = new_task
        return redirect('/')

    context = {'tasks': tasks, 'members': members, 'form': form}
    return render(request, 'tasks.html', context)

