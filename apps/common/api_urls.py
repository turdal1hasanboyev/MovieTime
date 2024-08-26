from django.urls import path

from .api.genre.GenreCreate.views import GenreCreateView
from .api.genre.GenreDestroy.views import GenreDestroyView
from .api.genre.GenreDetail.views import GenreRetrieveView
from .api.genre.GenreList.views import GenreListView
from .api.genre.GenreUpdate.views import GenreUpdateView

from .api.category.CategoryCreate.views import CategoryCreateView
from .api.category.CategoryDestroy.views import CategoryDestroyView
from .api.category.CategoryDetail.views import CategoryRetrieveView
from .api.category.CategoryList.views import CategoryListView
from .api.category.CategoryUpdate.views import CategoryUpdateView

from .api.award.AwardLC.views import AwardLCView
from .api.award.AwardRUD.views import AwardRUDView

from .api.actor.ActorLC.views import ActorLCView
from .api.actor.ActorRUD.views import ActorRUDView

from .api.country.CountryList.views import CountryListView


app_name = "common"

urlpatterns = [
    path('genrecreate/', GenreCreateView.as_view(), name='genre_create'),
    path('genredestroy/<str:name>/', GenreDestroyView.as_view(), name='genre_destroy'),
    path('genredetail/<str:name>/', GenreRetrieveView.as_view(), name='genre_detail'),
    path('genrelist/', GenreListView.as_view(), name='genre_list'),
    path('genreupdate/<str:name>/', GenreUpdateView.as_view(), name='genre_update'),

    path('categorycreate/', CategoryCreateView.as_view(), name="category_create"),
    path('categorylist/', CategoryListView.as_view(), name="category_list"),
    path('categoryupdate/<str:name>/', CategoryUpdateView.as_view(), name="category_edit"),
    path('categorydetail/<str:name>/', CategoryRetrieveView.as_view(), name="category_detail"),
    path('categorydelete/<str:name>/', CategoryDestroyView.as_view(), name="category_delete"),

    path('awardlc/', AwardLCView.as_view(), name='award_lc'),
    path('awardrud/<str:name>/', AwardRUDView.as_view(), name='award_rud'),

    path('actorlc/', ActorLCView.as_view(), name='actor_lc'),
    path('actorrud/<str:name>/', ActorRUDView.as_view(), name='actor_rud'),

    path('countrylist/', CountryListView.as_view(), name='country_list'),
]
