import requests 

class News:

  api_key = "be075abb31804a9a8dbe6783ff1b9cd1"
  api_url = "https://newsapi.org/v2/everything?apiKey={}".format(api_key)

  def __init__(self):
    pass

  def __str__(self):
    return "News Module"

  # Returns the top headlines of a certain topic
  def get(self, query):
    r = requests.get(url = self.api_url+"&q="+query).json()
    articles = r['articles']
    
    data = []
    for article in articles:
      data.append(
        {
          'title':article['title'],
          'url':article['url'],
          'source':article['source']['name'],
          'description':article['description'],
          'author':article['author']
        }
      )
    return data

  def getHeadlines(self, query, limit=-1):
    articles = self.get(query)
    print("************************")
    print("Top Headlines About {}".format(query))
    
    # if limit specified, trim number of articles
    if limit >= 0:
      articles = articles[:limit]
    
    print("************************")
    for article in articles:
      print(article['title'])
      print("Source: {} ({})".format(article['source'], article['url']))
      print("-----------------")
      
  
  