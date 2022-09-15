from django.db.models import Count, Sum
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, TemplateView, FormView, CreateView, UpdateView, DeleteView
from .forms import ContactForm, MusicianForm, AlbumForm
from .models import Musician, Album
from django.shortcuts import render, redirect


def album_list(request):
    return render(request, 'album_list.html', {})


class MusicianListView(ListView):
    model = Album
    context_object_name = "meus_musicos_favoritos"


class AlbumListView(ListView):
    model = Album
    allow_empty = True
    template_name = 'album.html'
    # albums = Album.objects.all()
    context_object_name = 'albums'


class AlbumDetailView(DetailView):
    queryset = Album.objects.all()
    template_name = 'album_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['musician_list'] = Musician.objects.all()
        return context


class AlbumCreateView(CreateView):
    template_name = 'album-form.html'
    form_class = AlbumForm
    success_url = reverse_lazy('list_album')


class AlbumUpdateView(UpdateView):
    model = Album
    fields = '__all__'
    template_name = 'album-form.html'
    success_url = reverse_lazy('list_album')


class AlbumDeleteView(DeleteView):
    model = Album
    success_url = reverse_lazy('list_album')


class AboutUs(TemplateView):
    template_name = 'aboutus.html'

    def get_context_data(self, *args, **kwargs):
        context = super(AboutUs, self).get_context_data(*args, **kwargs)
        context['email'] = 'nameofmycompany@gmail.com'
        context['phone'] = '+5521986245676'
        return context


class ContactFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    sucess_url = reverse_lazy('myapp:contact')

    def form_valid(self, form):
        form.send_email(form.cleaned_data)
        return super(ContactFormView, self).form_valid(form)

    def send_mail(self, valid_data):
        # send mail logic
        print(valid_data)
        pass


def list_musician(request):
    musicians = Musician.objects.all()
    number_of_musicians = Musician.objects.aggregate(sum_salary=Sum('salary'))
    data = {
        'musicians': musicians,
        'number_of_musicians': number_of_musicians
    }
    return render(request, 'musician.html', data)


def create_musician(request):
    form = MusicianForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_musician')

    return render(request, 'musician-form.html', {'form': form})


def update_musician(request, id):
    musician = Musician.objects.get(id=id)
    form = MusicianForm(request.POST or None, instance=musician)

    if form.is_valid():
        form.save()
        return redirect('list_musician')

    return render(request, 'musician-form.html', {'form': form, 'musician': musician})


def delete_musician(request, id):
    musician = Musician.objects.get(id=id)

    if request.method == 'GET':
        musician.delete()
        return redirect('list_musician')
    return redirect('list_musician')
