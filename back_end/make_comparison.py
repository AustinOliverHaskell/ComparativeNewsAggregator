class Comparison():

    def __init__(self, articles):
        self.articles = articles
        self.comparisons= []
        counter = 0
        for article in self.articles:
            for otherArticle in self.articles:
                if(article.title != otherArticle.title):
                    simKeys = set(article.keywords) & set(otherArticle.keywords)
                    if(len(simKeys) > 5):
                        Article1 = {article.title:{
                                    "URL":article.url,
                                    "Title":article.title,
                                    "Text":article.text,
                                    "Author":article.authors,
                                    "Leaning":" ",
                                    "keywords":article.keywords,
                                    "Rating":{
                                    "UP":0,
                                    "DOWN":0}}}
                        Article2 = {otherArticle.title:{
                                    "URL":otherArticle.url,
                                    "Title":otherArticle.title,
                                    "Text":otherArticle.text,
                                    "Author":otherArticle.authors,
                                    "Leaning":" ",
                                    "keywords":otherArticle.keywords,
                                    "Rating":{
                                    "UP":0,
                                    "DOWN":0}}}
                        counter = counter + 1
                        self.comparisons.append({counter:[Article1, Article2]})
        print(self.comparisons)


