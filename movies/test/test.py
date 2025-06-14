import requests
import environ
import os


def get_movies(url):
    res = requests.get(url)
    if 200 <= res.status_code < 400:
        return res.data
    else:
        raise Exception('no movies found')
    

def add_new_movie(url,movie:dict):
    res = requests.post(url,json={})

def check_movie_addtion(url,movie:dict):
    try:
        add_new_movie(url,movie=movie)
        movies =  get_movies(url)
        for k,v in movies.items():
            if k == 'name':
                if v == movie["name"]:
                    os.environ.TEST_RESULT = "OK"
                else:
                    os.environ.TEST_RESULT = "BAD"   
    except Exception as e:
            print(e)
            os.environ.TEST_RESULT = "BAD"     

if __name__ =='__main__':
    url= environ.get.APP_URL or 'localhost:8888/movie'
    movie={"id": 5, "name": "test movie", 'length': 120, 'genre': 'test'}
    check_movie_addtion(url,movie)