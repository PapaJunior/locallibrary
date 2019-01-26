from django.conf.urls import url

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/',views.BookListView.as_view(), name='books'),
    re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
]

