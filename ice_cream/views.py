from django.shortcuts import render, get_object_or_404, redirect

from .models import IceCream, Review
from .forms import CommentForm, ReviewForm


def index(request):
    template = 'ice_cream/index.html'
    selected_ice_creams = IceCream.objects.filter(on_main=True)
    # только то мороженое, у кторого есть флаг on_main
    context = {
        'selected_ice_creams': selected_ice_creams,
    }
    return render(request, template, context)


def ice_cream_list(request):
    template = 'ice_cream/ice_cream_list.html'
    ice_cream = IceCream.objects.filter()
    # все мороженое
    context = {
        'ice_creams': ice_cream,
    }
    return render(request, template, context)


def ice_cream_detail(request, pk):
    template = 'ice_cream/ice_cream_detail.html'
    ice_cream = get_object_or_404(IceCream, pk=pk)
    # Мороженое с id из запроса
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)

            comment.ice_cream = ice_cream
            comment.save()
            return redirect('ice_cream:ice_cream_detail', pk=pk)
    else:
        form = CommentForm()
    # Форма отправки данных для коментария
    context = {
        'ice_cream': ice_cream,
        'form': form,
    }
    return render(request, template, context)


def ice_cream_reviews(request):
    template = 'ice_cream/reviews.html'
    reviews = Review.objects.filter()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ice_cream:ice_cream_reviews')
    else:
        form = ReviewForm()
    context = {
        'form': form,
        'reviews': reviews,
    }
    return render(request, template, context)
