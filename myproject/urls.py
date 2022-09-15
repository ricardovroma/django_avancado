from django.contrib import admin
from django.urls import path
from myapp.views import album_list, AlbumListView, AlbumDetailView, AboutUs, ContactFormView, list_musician, \
    update_musician, create_musician, delete_musician, AlbumCreateView, AlbumUpdateView, AlbumDeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('album_list/', album_list, name='album-list'),
    # path('album_listview/', AlbumListView.as_view(), name='album-listview'),
    path('album_detailview/<slug:slug>/', AlbumDetailView.as_view(), name='album-detailview'),
    path('aboutus_templateview', AboutUs.as_view(), name='about-us-templateview'),
    path('contactus_formview', ContactFormView.as_view(), name='contact-us-formview'),
    path('musician/', list_musician, name='list_musician'),
    path('musician/create', create_musician, name='create_musician'),
    path('musician/update/<int:id>/', update_musician, name='update_musician'),
    path('musician/delete/<int:id>/', delete_musician, name='delete_musician'),
    path('album/', AlbumListView.as_view(), name='list_album'),
    path('album/<int:pk>/', AlbumDetailView.as_view(), name='detail_album'),
    path('album/create', AlbumCreateView.as_view(), name='create_album'),
    path('album/update/<int:pk>/', AlbumUpdateView.as_view(), name='update_album'),
    path('album/delete/<int:pk>/', AlbumDeleteView.as_view(), name='delete_album'),

]
