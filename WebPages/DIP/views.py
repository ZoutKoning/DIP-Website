from django.shortcuts import render
from django.http import HttpResponse

from .models import Sprint


def index(request):
    return render(request, 'DIP/index.html')
    # View for about page of site
    # Generate Sprint number
    # num_sprints = Sprint.sprint.count()
    # context = {
    # 'num_sprints': num_sprints,
    # }
    # return render(request, 'index.html', context=context)
