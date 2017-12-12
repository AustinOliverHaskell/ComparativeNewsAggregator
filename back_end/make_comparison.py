from comparison import Comparison

class FindComparisons():

    def __init__(self, articles):

        #Holds all the articles from the web scraper
        self.articles = articles

        #holds all the pairs of articles that are found to be similar
        self.comparisons= []

        #Holds all the keywords that appeared as matches
        self.keywords = []


        for key, value in self.articles.items():

            for otherKey, otherValue in self.articles.items():

                    if(key == otherKey):
                        continue

                    for article in value:

                        for otherArticle in otherValue:
                            #Finds the similar keywords between articles
                            simKeys = set(article.keywords) & set(otherArticle.keywords)

                            #We chose 4 by comapring what actual similar articles returned 
                            if(len(simKeys) >= 5):
                                #Tracks whether or not we've already found this match of articles before
                                alreadyMatched = False

                                #Check all the comparisons to make sure we haven't already found it 
                                for comparison in self.comparisons:
                                    if(comparison.getFirstArticle().title == article.title or comparison.getSecondArticle().title == article.title):
                                        alreadyMatched = True
                                        break

                                #A comparison tha has already been matched should not be added to control duplicates
                                if not alreadyMatched:
                                    self.comparisons.append(Comparison(article, otherArticle, simKeys))




        '''
        #Check each article's keywords against all the other keywords to find similar articles
        for article in self.articles:
            for otherArticle in self.articles:
                #ignore the same article which will be a perfect match
                if(article.title != otherArticle.title):
                    #Finds the similar keywords between articles
                    simKeys = set(article.keywords) & set(otherArticle.keywords)

                    #We chose 4 by comapring what actual similar articles returned 
                    if(len(simKeys) >= 5):
                        #Tracks whether or not we've already found this match of articles before
                        alreadyMatched = False

                        #Check all the comparisons to make sure we haven't already found it 
                        for comparison in self.comparisons:
                            if(comparison.getFirstArticle().title == article.title or comparison.getSecondArticle().title == article.title):
                                alreadyMatched = True
                                break

                        #A comparison tha has already been matched should not be added to control duplicates
                        if not alreadyMatched:
                            self.comparisons.append(Comparison(article, otherArticle, simKeys))
                            '''

        
    def getComparisons(self):
        return self.comparisons

    def getKeywords(self):
        return self.keywords


