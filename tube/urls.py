from django.urls import path
from . import views


app_name = "tube"
urlpatterns =[
    path('', views.index, name="index"),

    path('search/', views.search, name="search"),

    # TIPS:<型:変数名>とすることでビューに変数を与えることができる
    #idをuuidにするので、intをuuidに変える。

    path('single/<uuid:video_pk>/', views.single, name="single"),
    path('single_mod/<uuid:video_pk>/', views.single_mod, name="single_mod"),


    ##ランキングページ。DBからデータ抜き取って表示するだけ。GET文だけ
    path('rank/', views.rank, name="rank"),
    path('user_policy/', views.user_policy, name="user_policy"),

    # 以下認証済みユーザー専用
    path('video_comment_reply/<uuid:comment_pk>/', views.video_comment_reply, name="video_comment_reply"),
    path('video_comment_reply_to_reply/<uuid:videocommentreply_pk>/', views.video_comment_reply_to_reply,
         name="video_comment_reply_to_reply"),
    path('video_comment_edit/<uuid:comment_pk>/', views.video_comment_edit, name="video_comment_edit"),
    path('video_comment_reply_edit/<uuid:reply_pk>/', views.video_comment_reply_edit, name="video_comment_reply_edit"),
    path('video_comment_r_to_reply_edit/<uuid:r_to_reply_pk>/', views.video_comment_r_to_reply_edit,
         name="video_comment_r_to_reply_edit"),

    path('mypage/', views.mypage, name="mypage"),
    path('history/', views.history, name="history"),
    path('recommend/', views.recommend, name="recommend"),
    path('notify/', views.notify, name="notify"),
    path('mylist/', views.mylist, name="mylist"),
    path('upload/', views.upload, name="upload"),
    path('advertising_video/', views.advertising_video, name="advertising_video"),

    path('config/', views.config, name="config"),
    path('videoreport/<uuid:pk>/', views.videoreport, name="videoreport"),
    path('video_comment_report/<uuid:pk>/', views.video_comment_report, name="video_comment_report"),
    path('video_comment_reply_report/<uuid:pk>/', views.video_comment_reply_report, name="video_comment_reply_report"),
    path('video_comment_reply_to_reply_report/<uuid:pk>/', views.video_comment_reply_to_reply_report, name="video_comment_reply_to_reply_report"),

    path('usersingle/<uuid:pk>/', views.usersingle, name="usersingle"),
    path('userfollow/<uuid:pk>/', views.userfollow, name="userfollow"),
    path('userblock/<uuid:pk>/', views.userblock, name="userblock"),
    path('invite/<uuid:pk>/', views.invite, name="invite"),

    path('useredit/<uuid:pk>/', views.useredit, name="useredit"),
    path('comment_accept/', views.comment_accept, name="comment_accept"),
    path('single_video_comment_accept/<uuid:video_pk>/', views.single_video_comment_accept, name="single_video_comment_accept"),
    path('single_video_comment_refuse/<uuid:video_pk>/', views.single_video_comment_refuse, name="single_video_comment_refuse"),

    path('mylist_clear/', views.mylist_clear, name="mylist_clear"),
    path('mylist_one_each_clear/<uuid:pk>/', views.mylist_one_each_clear, name="mylist_one_each_clear"),
    path('comment_accept_one_each/<uuid:pk>/', views.comment_accept_one_each, name="comment_accept_one_each"),
    path('second_comment_accept_one_each/<uuid:pk>/', views.second_comment_accept_one_each, name="second_comment_accept_one_each"),
    path('third_comment_accept_one_each/<uuid:pk>/', views.third_comment_accept_one_each, name="third_comment_accept_one_each"),

    path('comment_delete_one_each/<uuid:pk>/', views.comment_delete_one_each,name="comment_delete_one_each"),
    path('second_comment_delete_one_each/<uuid:pk>/', views.second_comment_delete_one_each, name="second_comment_delete_one_each"),
    path('third_comment_delete_one_each/<uuid:pk>/', views.third_comment_delete_one_each, name="third_comment_delete_one_each"),
    path('single_video_comment_approval1/<uuid:video_pk>/', views.single_video_comment_approval1, name="single_video_comment_approval1"),
    path('single_video_comment_approval2/<uuid:video_pk>/', views.single_video_comment_approval2, name="single_video_comment_approval2"),
    path('comment_approval1/', views.comment_approval1, name="comment_approval1"),
    path('comment_approval2/', views.comment_approval2, name="comment_approval2"),

    #動画コメント既読処理
    path('comment_already_read/', views.comment_already_read, name="comment_already_read"),
    path('comment_already_read_1/', views.comment_already_read_1,name="comment_already_read_1"),
    path('comment_delete/', views.comment_delete, name="comment_delete"),

    #掲示板usersingle.html
    path('topic/<uuid:pk>/', views.topic, name="topic"),

    #広告動画
    path('advertising_videoreport/<uuid:pk>/', views.advertising_videoreport, name="advertising_videoreport"),
    path('advertising_video_single/<uuid:video_pk>/', views.advertising_video_single, name="advertising_video_single"),
    path('advertising_video_mod/<uuid:video_pk>/', views.advertising_video_mod, name="advertising_video_mod"),

]
