import requests
import json
import time

# TMDB API 키 설정
API_KEY = '381449cba8c79e4cf47ed87b999ac3f1'
BASE_URL = 'https://api.themoviedb.org/3'

# 영화 데이터 저장 리스트
movies_data = []

# 영화 세부 정보 및 배우/감독 정보 가져오기
def fetch_movie_credits(movie_id):
    response = requests.get(f"{BASE_URL}/movie/{movie_id}/credits", params={
        'api_key': API_KEY,
        'language': 'ko-KR'
    })

    if response.status_code == 200:
        data = response.json()
        # 감독 정보 추출
        director_data = next(
            (crew for crew in data.get('crew', []) if crew.get('job') == 'Director'), 
            None
        )
        director = {
            "name": director_data['name'],
            "profile_path": f"https://image.tmdb.org/t/p/w500{director_data['profile_path']}" 
            if director_data and director_data.get('profile_path') else None
        } if director_data else None

        # 배우 정보 추출 (상위 5명)
        cast = [
            {
                "name": actor['name'],
                "profile_path": f"https://image.tmdb.org/t/p/w500{actor['profile_path']}" if actor.get('profile_path') else None
            }
            for actor in data.get('cast', [])[:5]
        ]
        return director, cast
    else:
        print(f"Error fetching credits for movie_id {movie_id}: {response.status_code}")
        return None, []

# 영화 세부 정보 및 런타임 가져오기
def fetch_movie_details(movie_id):
    response = requests.get(f"{BASE_URL}/movie/{movie_id}", params={
        'api_key': API_KEY,
        'language': 'ko-KR'
    })

    if response.status_code == 200:
        data = response.json()
        runtime = data.get('runtime')  # 런타임 정보 (분 단위)
        return runtime
    else:
        print(f"Error fetching details for movie_id {movie_id}: {response.status_code}")
        return None

# API 호출 및 데이터 저장 함수
def fetch_movie_data():
    page = 1
    total_pages = 1  # 첫 번째 API 호출 후 실제 총 페이지 수로 업데이트될 예정

    while page <= total_pages:
        response = requests.get(f"{BASE_URL}/discover/movie", params={
            'api_key': API_KEY,
            'language': 'ko-KR',  # 한국어로 데이터를 요청합니다.
            'sort_by': 'popularity.desc',  # 인기도 순으로 정렬
            'vote_count.gte': 150,  # 투표수 170 이상 필터링
            'page': page
        })

        if response.status_code == 200:
            data = response.json()
            movies = data.get('results', [])
            for movie in movies:
                # 런타임, 감독, 배우 정보 가져오기
                runtime = fetch_movie_details(movie['id'])
                director, cast = fetch_movie_credits(movie['id'])

                movie_entry = {
                    "model": "movies.movie",
                    "pk": movie['id'],
                    "fields": {
                        "title": movie['title'],
                        "overview": movie['overview'],
                        "genres": movie['genre_ids'],
                        "release_date": movie['release_date'],
                        "popularity": movie['popularity'],
                        "vote_average": movie['vote_average'],
                        "vote_count": movie['vote_count'],
                        "poster_path": movie['poster_path'],
                        "backdrop_path": movie['backdrop_path'],
                        "adult": movie['adult'],
                        "runtime": runtime,  # 런타임 추가
                        "director": director,  # 감독 정보 추가 (이름과 사진)
                        "cast": cast  # 배우 이름과 사진 추가
                    }
                }
                movies_data.append(movie_entry)
            
            # 페이지 수 갱신
            if page == 1:
                total_pages = data.get('total_pages', 1)
            
            page += 1
            time.sleep(0.5)  # API 호출 간 딜레이를 추가하여 서버 부하를 줄입니다.
        else:
            print(f"Error fetching data for page {page}: {response.status_code}")
            break

# 영화 데이터 가져오기
fetch_movie_data()

# JSON 파일로 저장
with open('movies_with_director_and_cast.json', 'w', encoding='utf-8') as json_file:
    json.dump(movies_data, json_file, ensure_ascii=False, indent=4)

print("데이터 수집 및 저장이 완료되었습니다.")