from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import TypeOfKnotForm
from .models import Knot, TypeOfKnot

# Create your views here.
def about(request):
  return render(request, 'about.html')


def home(request):
  return render(request, 'home.html')


def knots_index(request):
  knots = Knot.objects.all()
  return render(request, 'knots/index.html', {'knots': knots})


def knots_detail(request, knot_id):
  knot = Knot.objects.get(id=knot_id)
  add_type_form = TypeOfKnotForm()
  return render(request, 'knots/detail.html', {'knot': knot, 'add_type_form': add_type_form})


# class-based views
class KnotCreate(CreateView):
  model = Knot
  fields = '__all__'


class KnotUpdate(UpdateView):
  model = Knot
  fields = '__all__'

class KnotDelete(DeleteView):
  model = Knot
  success_url = '/knots'


# def add_knot(request, add_knot):
#   pass