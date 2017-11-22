import newspaper
from newspaper import Article
from firebase import *

class UpdateFirebase():

	def __init__(self):
	
		# List of websites to scrape for article information
		self.websites = ["http://cnn.com/", "https://www.huffingtonpost.com/", 
						 "http://www.breitbart.com/", "http://www.foxnews.com/",
						 "https://www.reuters.com/", "http://occupydemocrats.com/"]
			
		# Connection to firebase database			 
        self.firebase = firebase.FirebaseApplication('https://newsapp-5d5a8.firebaseio.com/', None)
		
		# Holders for article URLs and entries for firebase database
		self.articles = []
		self.entries = {}
		
		# Sequence to get articles, scrape information, and post to database
		self._getArticles()
		self._getDataInformatics()
		self._formulateDatabaseResponse()
		self._postDatabaseResponse()
		
		
	def _getArticles(self):
	
		# Find all articles on each website and add URLs to list
		for website in self.websites:
			
			paper = newspaper.build(website)
			
			for article in paper.articles:
			
				self.articles.append(article.url)
				
	
	def _getDataInformatics(self):
	
		# For each article URL, scape web and formulate database response
		for id, article in enumerate(self.articles):
		
			_formulateDatabaseResponse(id, article)
			
			print('Formulating responses... %d% complete' % id / len(self.articles))
			
			
	def _formulateDatabaseResponse(self, id, article):

		news_article = Article(article.url)
		news_article.download()
		news_article.parse()
		news_article.nlp()
	
		entries["Articles"]["article_%d" % id] = {
		
			"URL" : article.url, "Title": new_article.title,
			"Text": news_article.text, "Author": news_article.author,
			"Leaning": "", "Rating": {"UP": 0, "DOWN": 0},
		}


if __name__ == "__main__":

    UpdateFirebase()
		
	
		
			
		
			
	
		
