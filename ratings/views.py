from django.shortcuts import render, get_object_or_404, redirect
from .models import Conference, Rating
from .forms import RatingForm
from django.db.models import Avg, Count

def index(request):
    conferences = Conference.objects.all()
    return render(request, 'index.html', {'conferences': conferences})

def conference_detail(request, slug):
    conference = get_object_or_404(Conference, unique_url=slug)
    is_saved = request.GET.get('saved') == 'true'

    rating_stats = conference.ratings.aggregate(
        average_rating=Avg('rating'),
        rating_count=Count('id')
    )

    context = {
        'conference': conference,
        'is_saved': is_saved,
        'average_rating': rating_stats['average_rating'],
        'rating_count': rating_stats['rating_count'],
    }

    return render(request, 'ratings/conference_detail.html', context)

def submit_rating(request, slug):
    conference = get_object_or_404(Conference, unique_url=slug)
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.conference = conference
            rating.save()
            return redirect(f"{conference.get_absolute_url()}?saved=true")

    else:
        form = RatingForm()
    return render(request, 'ratings/submit_rating.html', {'conference': conference, 'form': form})
