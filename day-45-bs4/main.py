from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
content = response.text

soup = BeautifulSoup(content, "html.parser")
articles = soup.find_all("span", class_="titleline")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.find("a").get("href")
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
print(article_texts)
print(article_links)
print(article_upvotes)

max_upvotes = max(article_upvotes)
max_index = article_upvotes.index(max_upvotes)
print(f"The most upvoted article is {article_texts[max_index]} | {article_links[max_index]}")