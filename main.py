from urllib import response
import requests
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

BASE_URL = "https://api.themoviedb.org/3/trending/movie/day"
API_KEY = os.getenv("API_KEY")
params = {
    "api_key": API_KEY
}

response = requests.get(
    BASE_URL,
    params=params,
)

response_json = response.json()

def print10trendingMovies():
    for i in range(10):
        print(response_json["results"][i]["title"])

print10trendingMovies()