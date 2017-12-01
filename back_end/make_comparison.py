class Comparison():

    def __init__(self, articles):

        #Holds all the articles from the web scraper
        self.articles = articles

        #holds all the pairs of articles that are found to be similar
        self.comparisons= []

        #Check each article's keywords against all the other keywords to find similar articles
        for article in self.articles:
            for otherArticle in self.articles:
                #ignore the same article which will be a perfect match
                if(article.title != otherArticle.title):
                    #Finds the similar keywords between articles
                    simKeys = set(article.keywords) & set(otherArticle.keywords)
                    #We chose 4 by comapring what actual similar articles returned 
                    if(len(simKeys) >= 5):
                        for comparison in self.comparisons:
                            for art in comparison:
                                
                                print(keys)
                                for key in keys:
                                    print(art[key]["Title"])
                        Article1 = {article.title:{
                                    "URL":article.url,
                                    "Title":article.title,
                                    "Text":article.text,
                                    "Author":article.authors,
                                    "Leaning":" ",
                                    "Keywords":article.keywords,
                                    "Rating":{
                                    "UP":0,
                                    "DOWN":0},
                                    "Comparisons":[]}}
                        Article2 = {otherArticle.title:{
                                    "URL":otherArticle.url,
                                    "Title":otherArticle.title,
                                    "Text":otherArticle.text,
                                    "Author":otherArticle.authors,
                                    "Leaning":" ",
                                    "Keywords":otherArticle.keywords,
                                    "Rating":{
                                    "UP":0,
                                    "DOWN":0},
                                    "Comparisons":[]}}

                        
                        self.comparisons.append([Article1, Article2])
                        print(simKeys)
                        #print(article.title)
                        #print(otherArticle.title)
        for comparison in self.comparisons:
            for temp in comparison:
                pass
    
    def getComparisons(self):
        return self.comparisons


