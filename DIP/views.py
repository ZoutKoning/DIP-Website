"""from django.shortcuts import render
from .models import Sprint
def index (request):
    View for about page of site
    #Generate Sprint number
    num_sprints = Sprint.sprint.count()
    context = {
        'num_sprints': num_sprints,
    }
    return render(request, 'index.html', context=context) """

from django.shortcuts import redirect
def index(request):
    return redirect('/About')