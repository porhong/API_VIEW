from rest_framework.response import Response
from .models import Movie
from .seriliazers import MovieSeriliazer
from rest_framework.views import APIView
from rest_framework import status


class MovieApiView(APIView):

    def get(self, request):
        movie = Movie.objects.all()
        serilaizer = MovieSeriliazer(movie, many=True)
        return Response(serilaizer.data)
    
        # return Response({"result","Hello"})
    def post(self, request) :
        new_Movie = MovieSeriliazer(data=request.data)
        if new_Movie.is_valid():
            new_Movie.save()
            return Response({"Message" : "New Movie has been created"}, status= status.HTTP_201_CREATED)
        
        return Response ({"Message":"Invalid data"}, status=status.HTTP_400_BAD_REQUEST)
    
class MovieDetailApiView(APIView):
    def get(self,request, id):
        movie = Movie.objects.get(pk=id)
        seriliazer = MovieSeriliazer(movie)
        return Response(seriliazer.data)
    def put(self, request, id) :
        movie = Movie.objects.get(pk=id)
        serializer = MovieSeriliazer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request, id) :
         movie = Movie.objects.get(pk=id)
         movie.delete()
         return Response({"Message" : "Movies has been deleted."},status=status.HTTP_200_OK)