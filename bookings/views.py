import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.db.models.query_utils import Q
from django.http.response import HttpResponse, JsonResponse
from django.views.generic import ListView, DetailView, View
from django.shortcuts import render
from.models import *
# Create your views here.


class MovieList(View):
    """View to show a dropdown of movies """

    def get(self, request):
        movies = Movie.objects.all()
        return render(request, 'movies.html', {'movies': movies})


class DatePicker(View, ):
    def get(self,  request, **args,):
        print(datetime.date.today())
        context = {}
        context["currentDate"] = datetime.datetime.strftime(
            datetime.date.today(), "%Y-%m-%d")
        context['maxDate'] = datetime.datetime.strftime(datetime.date.today() +
                                                        datetime.timedelta(days=5), "%Y-%m-%d")

        print(context)
        print(args.get('name'))
        return render(request, 'datepicker.html', context)


class TimePicker(View):
    def get(self, request, **args):
        name = args.get('name')
        date = args.get('date')
        print(name, date)
        context = {}
        movie = Movie.objects.get(name=name)
        now_time = datetime.time()
        print(now_time)
        shows = Show.objects.filter(Q(movie=movie) & Q(date=date))
        for show in shows:
            if(now_time < show.time):
                print('the show is in future')
                print(show.time)
            elif(now_time > show.time):
                print('the show is in past')
                print(show.time)

        context['shows'] = shows
        print(context)
        return render(request, 'timepicker.html', context)


class Booking(View):
    def get(self, request, **args):
        # # show_id = int(args.get('show'))
        # show = Show.objects.get(id=show_id)
        print(args.get('time'))
        return render(request, 'booking.html')

    def post(self, request, **args):
        return HttpResponse("Booking")


class SelectSeats(View):
    def get(self, request, **args):
        time = args.get('time')
        name = args.get('name')
        date = args.get('date')
        context = {}
        movie = Movie.objects.get(name=name)
        now_time = datetime.time()
        print(time)
        show = Show.objects.get(id=int(time))
        print(show)
        seats = Seat.objects.filter(show=show)
        print(seats)
        context['seats'] = seats
        return render(request, 'selectseats.html', context)


@method_decorator(csrf_exempt, name='dispatch')
class PromoCodes(View):
    def post(self, request, **args):
        body = json.loads(request.body.decode('utf-8'))
        promocode = body['promoCode']
        print(promocode)

        code = PromoCode.objects.filter(code=promocode).first()
        print
        if(code.is_active):
            return JsonResponse('Promo code is valid', status=200)
        else:
            return JsonResponse({'error': 'Promo code is not valid'}, status=400)
        # return JsonResponse({'error': 'Promo code is not valid'}, status=400)
