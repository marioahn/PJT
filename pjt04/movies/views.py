from django.shortcuts import render
import requests
import random
# Create your views here.
def recommendations(request):
    data = recommendation()
    context = {
        'title' : data[0],
        'img' : data[1],
        'overview': data[2],
        'release_date' : data[3],
        'score' : data[4],
        'id' : data[5],
    }

    return render(request, 'movies/recommendations.html', context)


def index(request):

    return render(request, 'movies/index.html')


def recommendation():
    url = 'https://api.themoviedb.org/3'
    path = '/movie/278/recommendations'

    params = {
        'api_key' : 'b5a5f84ebb682062b887779904a32def',
        'language' : 'ko'
    
    }
    # 요청 및 응답
    response = requests.get(url+path, params=params).json()
    results = response.get('results')

    n = random.choice(results)
    movie_title = n.get('title')
    movie_overview = n.get('overview')
    movie_release_date = n.get('release_date')
    movie_img = n.get('poster_path')
    movie_score = n.get('vote_average')
    movie_id = n.get('id')
    

    return movie_title, movie_img, movie_overview, movie_release_date, movie_score, movie_id
