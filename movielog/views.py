from django.shortcuts import get_object_or_404, render
from .models import Movielog
# Create your views here.

def home(request):
    movielog = Movielog.objects
    return render(request, 'home.html',{'movielogs': movielog})

def detail(request, movielog_id):
    movielog_detail = get_object_or_404(Movielog, pk=movielog_id)
    return render(request, 'detail.html', {'movielog':movielog_detail})