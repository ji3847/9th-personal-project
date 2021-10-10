from django.shortcuts import get_object_or_404, render, redirect
from .models import Movielog, HashTag
from django.utils import timezone
from .forms import MovielogForm, CommentForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings

# Create your views here.

def main(request):
    
    return render(request, 'main.html')

def home(request):
    movielog = Movielog.objects
    return render(request, 'home.html',{'movielogs': movielog})

def detail(request, movielog_id):
    movielog_detail = get_object_or_404(Movielog, pk=movielog_id)
    return render(request, 'detail.html', {'movielog':movielog_detail})


def new(request):
    form = MovielogForm()
    return render(request, 'new.html', {'form': form})


def create(request):
    form = MovielogForm(request.POST, request.FILES)
    print(form)
    if form.is_valid():
        new_movielog = form.save(commit=False)
        new_movielog.pub_date = timezone.now()
        new_movielog.save()
        hashtags = request.POST['hashtags']
        hashtag = hashtags.split(",")
        for tag in hashtag:
            ht = HashTag.objects.get_or_create(hashtag_name=tag)
            new_movielog.hashtag.add(ht[0])

        return redirect('detail', new_movielog.id)
    return redirect('home')


def edit(request, movielog_id):
    movielog_detail = get_object_or_404(Movielog, pk=movielog_id)
    return render(request, 'edit.html', {'movielog':movielog_detail})



def update(request, movielog_id):
    movielog_update = get_object_or_404(Movielog, pk=movielog_id)
    movielog_update.title = request.POST['title']
    movielog_update.director = request.POST['director']
    movielog_update.release_day = request.POST['release_day']
    movielog_update.body = request.POST['body']
    movielog_update.image = request.POST['image']
    movielog_update.save()
    return redirect('home')


def delete(request, movielog_id):
    movielog_delete = get_object_or_404(Movielog, pk=movielog_id)
    movielog_delete.delete()
    return redirect('home')


def add_comment_to_post(request, movielog_id):
    movielog = get_object_or_404(Movielog, pk=movielog_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = movielog
            comment.save()
            return redirect('detail', movielog_id)
    else :
        form = CommentForm()
    return render(request, 'add_comment_to_post.html', {'form':form})


    

def detail(request, movielog_id):
    movielog_detail = get_object_or_404(Movielog, pk=movielog_id)
    movielog_hashtag = movielog_detail.hashtag.all()
    return render(request, 'detail.html', {'movielog':movielog_detail,'hashtags':movielog_hashtag})

