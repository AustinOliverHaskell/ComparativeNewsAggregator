import newspaper
from newspaper import Article
from make_comparison import FindComparisons
from update_firebase import UpdateFirebase

class WebScraper():

	def __init__(self):
	
		# List of websites to scrape for article information
		self.websites = ["http://cnn.com", "http://www.huffingtonpost.com", 
						 "http://www.breitbart.com", "http://www.foxnews.com",
						 "http://www.reuters.com", "http://occupydemocrats.com/"]
		
		# Holders for article URLs and entries for firebase database
		self.urls = {'http://cnn.com':[],
					 'http://www.huffingtonpost.com':[],
					 'http://www.breitbart.com':[], 
					 'http://www.foxnews.com':[], 
					 'http://www.reuters.com':[], 
					 'http://occupydemocrats.com/':[]}
		self.articles = {'http://cnn.com':[],
					     'http://www.huffingtonpost.com':[],
					 	 'http://www.breitbart.com':[], 
					 	 'http://www.foxnews.com':[], 
					 	 'http://www.reuters.com':[], 
					 	 'http://occupydemocrats.com/':[]}
		self.entries = {}
		
		# Sequence to get articles and scrape information
		self._getURLs()
		self._getDataInformatics()
		self.comparison = FindComparisons(self.articles)

		self.upfb = UpdateFirebase(self.comparison.getComparisons())
		
		
	def _getURLs(self):
	
		# Find all articles on each website and add URLs to list
		for website in self.websites:
			
			paper = newspaper.build(website, memoize_articles=False)
			
			for article in paper.articles:
			
				self.urls[website].append(article.url)
				
		print("There were ", len([value for key, value in self.urls.items()]), " urls found.")
				
	
	def _getDataInformatics(self):
	
		# For each article URL, scrape web and formulate database response
		for key, value in self.urls.items():
			counter = 0
			for url in value:
				self._formulateDatabaseResponse(url, key)
				counter += 1
				print("Scraping from %s is %f percent done..." % (key, (counter * 100 / len(value))))
			
			
			
			
	def _formulateDatabaseResponse(self, article, website):

		# Create a news article for each article URL
		news_article = Article(article)
		
		# Parse article for web scraping information
		news_article.download()
		try:
			news_article.parse()
		except Exception:
			print("Exception Caught")
			return
		news_article.nlp()

		self.articles[website].append(news_article)



if __name__ == "__main__":

    WebScraper()
		
	
		
			
		
			
	
		
