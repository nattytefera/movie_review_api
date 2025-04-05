import requests
response = requests.get(
    "https://api.themoviedb.org/3/movie/550?api_key=e7a665c9311f472a412e0c0585846837"
)
print(response.json())