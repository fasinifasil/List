from .import views
from django.urls import path
app_name='app1'
urlpatterns = [
    path('',views.index,name='index'),
    path('movie/<int:movie_id>/',views.detail,name='detail'),
    path('add',views.add,name='add'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
    path('classhome',views.MovieListView.as_view(),name='classhome'),
    path('classdetail/<int:pk>/',views.MovieDetailView.as_view(),name='classdetail'),
    path('classupdate/<int:pk>/',views.MovieUpdateView.as_view(),name='classupdate'),
    path('classdelete/<int:pk>/',views.MovieDeleteView.as_view(),name='classdelete'),
    path('mailview',views.emailsend,name='emailsend')
]
