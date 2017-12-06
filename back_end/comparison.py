class Comparison():

    def __init__(self, article1, article2, matchingKeywords):
        self.article1 = article1
        self.article2 = article2
        self.matchingKeywords = matchingKeywords

    def getFirstArticle(self):
        return self.article1

    def getSecondArticle(self):
        return self.article2

    def getMatchingKeywords(self):
        return self.matchingKeywords