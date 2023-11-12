import requests

api_key = "39562f0f08d64611b7691cc765bab3bd"

url = ("https://newsapi.org/v2/everything?q=tesla&"
       "sortBy=publishedAt&"
       "apiKey=39562f0f08d64611b7691cc765bab3bd")

# Make request
request = requests.get(url)

# Get a dictionary with data
# request.text este class str, si arata ca si un dict, daca pun json este un dict si apare ca inainte
#content = request.text
content = request.json()

# Access the article titles and description
#print(type(content))
#print(content)
#print(content["articles"])

for article in content["articles"]:
    print(article["title"])
    print(article["description"])