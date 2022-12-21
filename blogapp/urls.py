from django.urls import path
from . import views

#URLconfのURLパターンを逆引きできるようにアプリ名を登録
app_name="blogapp"

#URLパターンを登録するためのリスト
urlpatterns = [
    
    path("",views.IndexView.as_view(),name="index"),

    #詳細ページのURLパターン
    path("blog-detail/<int:pk>/",views.BlogDetail.as_view(),name="blog_detail"),

    #ScienceカテゴリのURL
    path("science-list/", views.ScienceView.as_view(), name="science_list"),

    #FoodカテゴリのURL
    path("food-list/", views.FoodView.as_view(), name="food_list"),

    #musicカテゴリのURL
    path("music-list/", views.MusicView.as_view(), name="music_list"),

    #問い合わせページのURLパターン
    path("contact/",views.ContactView.as_view(),name="contact")
]
