from django.urls import path

from .api.tag.TagLC.views import TagLCView
from .api.tag.TagRUD.views import TagRUDView

from .api.movienews.MovieNewsCreate.views import MovieNewsCreateView
from .api.movienews.MovieNewsDestroy.views import MovieNewsDestroyView
from .api.movienews.MovieNewsDetail.views import MovieNewsRetrieveView
from .api.movienews.MovieNewsList.views import MovieNewsListView
from .api.movienews.MovieNewsUpdate.views import MovieNewsUpdateView


app_name = "news"

urlpatterns = [
    path("taglc/", TagLCView.as_view(), name="tag_lc"),
    path("tagrud/<str:name>/", TagRUDView.as_view(), name="tag_rud"),

    path("movienewscreate/", MovieNewsCreateView.as_view(), name="movie_news_create"),
    path("movienewsdestroy/<slug:slug>/", MovieNewsDestroyView.as_view(), name='movie_news_destroy'),
    path("movienewsdetail/<slug:slug>/", MovieNewsRetrieveView.as_view(), name='movie_news_detail'),
    path("movienewslist/", MovieNewsListView.as_view(), name='movie_news_list'),
    path("movienewsupdate/<slug:slug>/", MovieNewsUpdateView.as_view(), name='movie_news_update'),
]
