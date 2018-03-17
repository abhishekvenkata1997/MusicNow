from django.contrib.auth.decorators import login_required
from django.views import generic
from .models import Album,Song
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
from django.views.generic import View
from .forms import UserForm
from django.contrib.auth.mixins import LoginRequiredMixin

class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = "all_albums"

    def get_queryset(self):
        return Album.objects.all()

class IndexView1(generic.ListView):
    template_name = 'music/index1.html'
    context_object_name = "all_songs"

    def get_queryset(self):
        return Song.objects.all()

class DetailView(generic.DetailView):

    template_name = 'music/detail.html'
    model = Album



class AlbumCreate(CreateView):
    model = Album
    fields = ['artist','album_logo','genre','album_title']

class AlbumUpdate(UpdateView):
    model = Album
    fields = ['artist','album_logo','genre','album_title']

class AlbumDelete(DeleteView,LoginRequiredMixin):
     model = Album
     raise_exception = True
     success_url = reverse_lazy('music:index')
  #  raise_exception = True


class SongCreate(CreateView):
    model = Song
    fields = ['song_title','song_length','album','is_Favorite']



class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration.html'

    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form })

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit = False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()


            user = authenticate(username = username,password = password)
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('music:login')
        return render(request,self.template_name,{'form':form})

def search(request):

     if request.user.is_authenticated:
        albums = Album.objects.all()
        songs = Song.objects.all()
        query = request.GET.get("q")

        if query:
            albums = albums.filter(
                Q(album_title__icontains = query)|
                Q(artist__icontains = query)
                ).distinct()

            songs = songs.filter(
            Q(song_title__icontains = query),
            ).distinct()

            return render(request,'music/search.html',{
            'albums':albums,
            'songs':songs,
            'query' : query,
            })
        else:
            return(request,'music/search.html' ,{
            'albums' : albums})



def logoutuser(request):
    logout(request)
    form  = UserForm(request.POST or None)
    return render(request,'music/logout.html',{'form':form})



def loginuser(request):

    if request.method == "GET":
        return render(request,'music/login.html',{} )

    if  request.method == "POST" :

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username,password = password)

        if user is not None:
                return redirect('music:index')

        return render(request,'music/login.html',{ 'error' : 1 ,'username': "Username or Password is Incorrect" } )
    return render(request,'music/login.html',{'error': 1 })


def favorite(request, song_id):

    song = get_object_or_404(Song, pk = song_id)
    try:
        if song.is_Favorite  :
            song.is_Favorite = False
            song.save()
            return redirect("music:index1")
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/index1.html', {'song': song})

    else:
            song.is_Favorite = True
            song.save()
            return redirect("music:index1")



