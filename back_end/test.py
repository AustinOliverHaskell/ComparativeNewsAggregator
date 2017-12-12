import newspaper 
from newspaper import Article
from make_comparison import FindComparisons
from update_firebase import UpdateFirebase

articles = []
articles.append(Article('https://www.cnn.com/2017/12/01/politics/michael-flynn-charged/index.html'))
articles.append(Article('http://www.foxnews.com/politics/2017/12/01/michael-flynn-pleads-guilty-to-false-statements-charge-in-russia-probe.html'))

for article in articles:
    article.download()
    article.parse()
    article.nlp()

comparison = FindComparisons(articles)

upfb = UpdateFirebase(comparison.getComparisons())

