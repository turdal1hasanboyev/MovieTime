from django.urls import path

from .api.movie.MovieCreate.views import MovieCreateView
from .api.movie.MovieDelete.views import MovieDeleteView
from .api.movie.MovieUpdate.views import MovieUpdateView
from .api.movie.MovieList.views import MovieListView
from .api.movie.MovieDetail.views import MovieDetailView


app_name = "movie"

urlpatterns = [
    path('moviecreate/', MovieCreateView.as_view(), name='movie_create'),
    path('moviedelete/<slug:slug>/', MovieDeleteView.as_view(), name='movie_delete'),
    path('movieupdate/<slug:slug>/', MovieUpdateView.as_view(), name='movie_update'),
    path('movielist/', MovieListView.as_view(), name='movie_list'),
    path('moviedetail/<slug:slug>/', MovieDetailView.as_view(), name='movie_detail'),
]
