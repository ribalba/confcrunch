from django.db import models
from django.urls import reverse

class Conference(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()
    description = models.TextField()
    unique_url = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('conference_detail', kwargs={'slug': self.unique_url})

    def get_rating_submit_url(self):
        return reverse('submit_rating', kwargs={'slug': self.unique_url})

class Rating(models.Model):
    conference = models.ForeignKey(Conference, related_name='ratings', on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    email = models.EmailField()
    feedback = models.TextField()

    def __str__(self):
        return f'Rating {self.rating} for {self.conference.name}'
