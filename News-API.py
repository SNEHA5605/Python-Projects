import requests #pip install requests
query = input("What type of news are you interested in today?")
api = "5df5a79fca864336ad4ac31b0411922c"
url = f"https://newsapi.org/v2/everything?q={query}&from=2026-06-13&sortBy=publishedAt&apiKey={api}"
print(url)
r = requests.get(url)
data = r.json()
articles = data["articles"]
for index, article in enumerate(articles):
    print(index + 1,article["title"],article["url"])
    print("\n**********************************\n")
