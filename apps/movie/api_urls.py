from django.urls import path

from .api.movie.MovieCreate.views import MovieCreateView
from .api.movie.MovieDelete.views import MovieDeleteView
from .api.movie.MovieUpdate.views import MovieUpdateView
from .api.movie.MovieList.views import MovieListView
from .api.movie.MovieDetail.views import MovieDetailView

from .api.movieimage.MovieImageCreate.views import MovieImageCreateView
from .api.movieimage.MovieImageDestroy.views import MovieImageDestroyView
from .api.movieimage.MovieImageList.views import MovieImageListView
from .api.movieimage.MovieImageDetail.views import MovieImageRetrieveView
from .api.movieimage.MovieImageUpdate.views import MovieImageUpdateView


app_name = "movie"

urlpatterns = [
    path('moviecreate/', MovieCreateView.as_view(), name='movie_create'),
    path('moviedelete/<slug:slug>/', MovieDeleteView.as_view(), name='movie_delete'),
    path('movieupdate/<slug:slug>/', MovieUpdateView.as_view(), name='movie_update'),
    path('movielist/', MovieListView.as_view(), name='movie_list'),
    path('moviedetail/<slug:slug>/', MovieDetailView.as_view(), name='movie_detail'),

    path('movieimagecreate/', MovieImageCreateView.as_view(), name='movie_image_create'),
    path('movieimagedestroy/<str:movie>/', MovieImageDestroyView.as_view(), name='movie_image_delete'),
    path('movieimagelist/', MovieImageListView.as_view(), name='movie_image_list'),
    path('movieimagedetail/<str:movie>/', MovieImageRetrieveView.as_view(), name='movie_image_detail'),
    path('movieimageupdate/<str:movie>/', MovieImageUpdateView.as_view(), name="movie_image_update"),
]
