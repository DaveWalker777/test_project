from django.shortcuts import render
from django.shortcuts import  redirect
from .forms import PersonForm, RankForm
from .models import Person, Rank
# Create your views here.


def home(request):
    return render(request, 'task/home.html')


def management(request):
    persons = Person.objects.order_by('id')[::-1]
    return render(request, 'task/management.html',  {'title': 'Management', 'persons': persons})


def ranks(request):
    ranks = Rank.objects.order_by('id')[::-1]
    return render(request, 'task/ranks.html', {'title': 'Ranks', 'ranks': ranks})

def create_rank(request):
    error = ''
    if request.method == "POST":
        form = RankForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма содержит ошибки'
    form = RankForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'task/create_rank.html', context)


def create_person(request):
    error = ''
    if request.method == "POST":
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма содержит ошибки'
    form = PersonForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'task/create_person.html', context)


def update_person(request, person_id):
    person = Person.objects.get(pk=person_id)
    form = PersonForm(request.POST or None, instance=person)
    if form.is_valid():
        form.save()
        return redirect('management')
    return render(request, 'task/update_person.html', {'person': person,
                                                'form': form})


def delete_person(request, person_id):
    person = Person.objects.get(pk=person_id)
    person.delete()
    return redirect('management')


def update_rank(request, rank_id):
    rank = Rank.objects.get(pk=rank_id)
    form = RankForm(request.POST or None, instance=rank)
    if form.is_valid():
        form.save()
        return redirect('ranks')
    return render(request, 'task/update_rank.html', {'rank': rank,
                                                'form': form})


def delete_rank(request, rank_id):
    rank = Rank.objects.get(pk=rank_id)
    rank.delete()
    return redirect('ranks')