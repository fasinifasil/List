import kwargs as kwargs
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from django.urls import reverse_lazy

from .models import Movie
from .forms import MovieForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
from django.core.mail import send_mail



def index(request):
    movie=Movie.objects.all()
    context={
        'movie_list':movie
    }
    return render(request,'index.html',context)
def detail(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,'detail.html',{'movie':movie})

def add(request):
    if request.method == 'POST':
        name=request.POST.get('name',)
        desc=request.POST.get('desc',)
        year=request.POST.get('year',)
        image=request.FILES['image']
        movie=Movie(name=name,desc=desc,year=year,image=image)
        movie.save();
        return redirect('/')
    return render(request,'add.html')

def update(request,id):
    movie=Movie.objects.get(id=id)
    form=MovieForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})
def delete(request,id):
     if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
     return render(request,'delete.html')

class MovieListView(ListView):
    model = Movie
    template_name = 'index.html'
    context_object_name = 'movie_list'

class MovieDetailView(DetailView):
    model=Movie
    template_name = 'detail.html'
    context_object_name = 'movie'

class MovieUpdateView(UpdateView):
    model = Movie
    template_name = 'update.html'
    context_object_name = 'movie'
    fields =('name','desc','year','image')

    def get_success_url(self):
        return reverse_lazy('app1:classdetail',kwargs={'pk':self.object.id})
class MovieDeleteView(DeleteView):
    model = Movie
    template_name = 'delete.html'
    success_url = reverse_lazy('app1:classhome')

def emailsend(request):
    send_mail('Testing email','Testing message for program','fasinifasil@gmail.com',['mahase8883@kuvasin.com','bismina1995@gmail.com'],fail_silently=False,)
    return HttpResponse('email send')