# pjt04를 하면서 배운 것

1. 예전 관통프로젝트인 01~03 까지 복습을 할 수 있었다.
2. json 처리 방법이 기억나지 않아 recommendations를 구현하지 못했다.
3. json 데이터 처리 방법을 복습하려 다시보기를 했지만 만족할 만한 결과를 얻지 못했다.
4. 구글링을 통해 다시 복습을 하고, 코드를 작성했으나 None이 반환됨
```
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


5. 위의 함수를 viesw.py에 사용하여 받아와서 recommendation.html에 넘겨 출력함
6. json 데이터 처리가 힘들었지만, 구글링을 통해 완벽히 숙지했습니다!

