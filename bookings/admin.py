from django.contrib import admin

# Register your models here.
from .models import Movie, Bookings, PromoCode, Seat, Show
admin.site.register(Movie)
admin.site.register(Bookings)
admin.site.register(PromoCode)
admin.site.register(Show)
admin.site.register(Seat)
