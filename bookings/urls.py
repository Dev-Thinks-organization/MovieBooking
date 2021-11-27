from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views
urlpatterns = [
    path('', views.MovieList.as_view(),
         name='movies'),
    path('movies/<str:name>/', login_required(views.DatePicker.as_view(), login_url='/auth/login/'),
         name='movie_detail'),
    path('movies/<str:name>/<str:date>/',
         login_required(views.TimePicker.as_view(), login_url='/auth/login/'),),
    path('movies/<str:name>/<str:date>/<str:seat>',
         login_required(views.SelectSeats.as_view(), login_url='/auth/login/'), name='selectSeats'),
    path('movies/<str:name>/<str:date>/<str:time>/<str:seat>/',
         login_required(views.Booking.as_view(), login_url='/auth/login/'), name='booking'),
    path('promocode', views.PromoCodes.as_view(), name='promocode'),
]
