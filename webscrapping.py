import requests
from bs4 import BeautifulSoup
import pandas as pd
url ="https://books.toscrape.com/"
response= requests.get(url)
soup= BeautifulSoup(response.text, 'html.parser')
books=soup.find_all("article",class_="product_pod")
print(books[0])
data=[]
for book in books:
  title = book.h3.a["title"]
  price = book.find("p", class_="price_color").text
  data.append({
      "title":title,
      "price":price
  })
  df=pd.DataFrame(data)
  print(df.head())
  df['price'] =df['price'].str.replace('Â£','')
  df['price'] =df['price'].astype(float)
  price= (df['price']).mean()

  range=df[(df['price']>=price-2)&(df['price']<=price+2)]
  print(range)


