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

from .api.review.ReviewCreate.views import ReviewCreateView
from .api.review.ReviewDestroy.views import ReviewDestroyView
from .api.review.ReviewDetail.views import ReviewRetrieveView
from .api.review.ReviewList.views import ReviewListView
from .api.review.ReviewUpdate.views import ReviewUpdateView

from .api.liked.LikedCreate.views import LikedCreateView
from .api.liked.LikedDestroy.views import LikedDestroyView
from .api.liked.LikedList.views import LikedListView
from .api.liked.LikedDetail.views import LikedRetrieveView
from .api.liked.LikedUpdate.views import LikedUpdateView

from .api.additionaiInfo.AdditionalInfoCreate.views import AdditionalInfoCreateView
from .api.additionaiInfo.AdditionalInfoDelete.views import AdditionalInfoDestroyView
from .api.additionaiInfo.AdditionalInfoList.views import AdditionalInfoListView
from .api.additionaiInfo.AdditionalInfoDetail.views import AdditionalInfoDetailView
from .api.additionaiInfo.AdditionalInfoUpdate.views import AdditionalInfoUpdateView

from .api.moviefile.MovieFileLC.views import MovieFileLCView
from .api.moviefile.MovieFileRUD.views import MovieFileRUDView

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

    path('reviewcreate/', ReviewCreateView.as_view(), name='review_create'),
    path('reviewdestroy/<str:movie>/', ReviewDestroyView.as_view(), name='review_delete'),
    path('reviewlist/', ReviewListView.as_view(), name='review_list'),
    path('reviewdetail/<str:movie>/', ReviewRetrieveView.as_view(), name='review_detail'),
    path('reviewupdate/<str:movie>/', ReviewUpdateView.as_view(), name="review_update"),

    path('likedcreate/', LikedCreateView.as_view(), name="liked_create"),
    path('likeddestroy/<str:movie>/', LikedDestroyView.as_view(), name='liked_destroy'),
    path('likedlist/', LikedListView.as_view(), name='liked_list'),
    path('likeddetail/<str:movie>/', LikedRetrieveView.as_view(), name='liked_detail'),
    path('likedupdate/<str:movie>/', LikedUpdateView.as_view(), name="liked_update"),

    path("additionalinfocreate/", AdditionalInfoCreateView.as_view(), name="additional_info_create"),
    path("additionalinfodelete/<str:movie>/", AdditionalInfoDestroyView.as_view(), name='additional_info_delete'),
    path("additionalinfolist/", AdditionalInfoListView.as_view(), name='additional_info_list'),
    path("additionalinfodetail/<str:movie>/", AdditionalInfoDetailView.as_view(), name="additional_info_detail"),
    path("additionalinfoupdate/<str:movie>/", AdditionalInfoUpdateView.as_view(), name="additional_info_update"),

    path("moviefilelc/", MovieFileLCView.as_view(), name="moviefilelc"),
    path("moviefilerud/<str:movie>/", MovieFileRUDView.as_view(), name="moviefilelc"),
]
