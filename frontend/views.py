from django.shortcuts import render


def user_list(request):
    return render(request, 'frontend/user_list.html')


def members_list(request):
    return render(request, 'frontend/members_list.html')
