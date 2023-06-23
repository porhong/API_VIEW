from rest_framework import serializers
from .models import Movie

class MovieSeriliazer(serializers.HyperlinkedModelSerializer) :
    id = serializers.ReadOnlyField()
    class Meta :
        model = Movie
        fields = ['id','title', 'release_date']    