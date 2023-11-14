import requests
from send_email import send_emailll

api_key = "39562f0f08d64611b7691cc765bab3bd"
topic = "tesla"

url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&"
       "sortBy=publishedAt&"
       "apiKey=39562f0f08d64611b7691cc765bab3bd&"
       "language=ro")

# Make request
request = requests.get(url)

# Get a dictionary with data
# request.text este class str, si arata ca si un dict, daca pun json este un dict si apare ca inainte
# content = request.text
content = request.json()

# Access the article titles and description
# print(type(content))
# print(content)
# print(content["articles"])

content_email = "Subject: Stirile zilei" + "\n"
for article in content["articles"][:20]:
#   print(article["title"])
#   print(article["description"])

# Asta imi scoate doar un titlu cat si o descriere doar de la final..
#    content_email = article["title"] + "\n" + article["description"]

    if article["title"] is not None:
        content_email = content_email + article["title"] + "\n" \
                        + article["description"] + "\n" \
                        + article["url"] + 2*"\n"

#print(content_email)

# Pt UnicodeEncodeError: 'ascii' codec can't encode character '\u201d' in position 21: ordinal not in range(128)
content_email = content_email.encode("utf-8")

send_emailll(message=content_email)
