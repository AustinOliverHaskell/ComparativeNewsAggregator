import newspaper
from newspaper import Article

class WebScraper():

	def __init__(self):
	
		# List of websites to scrape for article information
		self.websites = ["http://cnn.com", "http://www.huffingtonpost.com", 
						 "http://www.breitbart.com", "http://www.foxnews.com",
						 "http://www.reuters.com", "http://occupydemocrats.com/"]
		
		# Holders for article URLs and entries for firebase database
		self.articles = []
		self.entries = {}
		
		# Sequence to get articles and scrape information
		self._getArticles()
		self._getDataInformatics()
		
		
	def _getArticles(self):
	
		# Find all articles on each website and add URLs to list
		for website in self.websites:
			
			paper = newspaper.build(website)
			
			for article in paper.articles:
			
				self.articles.append(article.url)

        print("There were ", len(self.articles), " articles found.")
				
	
	def _getDataInformatics(self):
	
		# For each article URL, scape web and formulate database response
		for id, article in enumerate(self.articles, 1):
		
			self._formulateDatabaseResponse(id, article)
			
			print('Formulating responses... %f percent complete' % (id * 100 / len(self.articles)))
			
			
	def _formulateDatabaseResponse(self, id, article):

		# Create a news article for each article URL
		news_article = Article(article)
		
		# Parse article for web scraping information
		news_article.download()
		news_article.parse()
		news_article.nlp()
	
		# Create JSON structure for database entry
		self.entries["article_%d" % id] = {
		
			"URL" : article, "Title": news_article.title,
			"Text": news_article.text, "Author": news_article.authors,
			"Leaning": "", "Rating": {"UP": 0, "DOWN": 0},
		}


if __name__ == "__main__":

    WebScraper()
		
	
		
			
		
			
	
		
