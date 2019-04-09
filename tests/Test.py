import newspaper
if __name__ == '__main__':
   web_paper = newspaper.build("https://www.sohu.com/", language="zh", memoize_articles=False)
   for article in web_paper.articles:
       print(article.url)
       print(article.title)