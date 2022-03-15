from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from fbuz_expert.forms import ExpForm, ExportForm
from .models import Expertises
from django.db.models import Q
from django.core.paginator import Paginator
from datetime import datetime, date


@login_required
def index(request):
    all_expertises = Expertises.objects.all()[::-1]
    # paginator_all = Paginator(all_expertises, 10)

    creator = request.user.pk
    your_expertises = Expertises.objects.filter(creator=creator)[::-1]

    # paginator_your = Paginator(your_expertises, 13)

    # page_number = request.GET.get('page')
    # page_obj_all = paginator_all.get_page(page_number)
    # page_obj_your = paginator_your.get_page(page_number)

    if request.method == 'POST':
        fulltext_search = request.POST.get('anything')

        if fulltext_search:
            search_date = Expertises.objects.filter(
                Q(pk__icontains=fulltext_search) |
                Q(object_name__icontains=fulltext_search) |
                Q(exp_basis__icontains=fulltext_search) |
                Q(exp_subject__icontains=fulltext_search) |
                Q(exp_result__icontains=fulltext_search) |
                Q(executor_name__icontains=fulltext_search) |
                Q(recipient_name__icontains=fulltext_search) |
                Q(created__icontains=fulltext_search.format('Y-m-d'))
            )

            return render(request, 'search.html', {'search_date': search_date})

    return render(request, 'index.html', {'all_expertises': all_expertises,
                                          'your_expertises': your_expertises,
                                          # 'page_obj_all': page_obj_all,
                                          # 'page_obj_your': page_obj_your,
                                          }
                  )


@login_required()
def expertise(request, pk):
    exp = Expertises.objects.get(pk=pk)

    if request.method == 'POST':
        form = ExpForm(request.POST, request.FILES, instance=exp)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ExpForm(instance=exp)

    return render(request, 'expertise.html', {'form': form, 'exp': exp})


@login_required
def add_exp(request):
    last_exp = Expertises.objects.latest('pk')
    exp_last_number = last_exp.exp_number
    last_exp_year = last_exp.created.year

    if datetime.now().year != last_exp_year:
        exp_last_number = 1

    if Expertises.objects.count() is None:
        exp_last_number = 1
    else:
        exp_last_number += 1

    if request.method == 'POST':
        form = ExpForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.creator = request.user
            post.exp_number = exp_last_number
            post.save()
            return redirect('index')
    else:
        form = ExpForm()

    return render(request, 'add_exp.html', {'form': form})


@login_required()
def export(request):
    if request.method == 'POST':
        form = ExportForm(request.POST)
        if form.is_valid():
            form.cleaned_data()
            # print(form)
    else:
        form = ExportForm()

    return render(request, 'export.html', {'form': form})


@login_required()
def snake(request):
    return render(request, 'snake.html')
