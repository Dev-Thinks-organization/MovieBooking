from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
urlpatterns = [
    path('', login_required(views.MovieList.as_view(),
         login_url='/auth/login/'), name='movies'),
    path('movies/<str:name>/', login_required(views.DatePicker.as_view(),),
         name='movie_detail'),
    path('movies/<str:name>/<str:date>/',
         login_required(views.TimePicker.as_view(),),),
    path('movies/<str:name>/<str:date>/<str:time>',
         login_required(views.SelectSeats.as_view(),), name='booking'),
    path('movies/<str:name>/<str:date>/<str:time>/<str:seat>',
         login_required(views.Booking.as_view(),), name='booking'),
    path('promocode', views.PromoCodes.as_view(), name='promocode'),
]
