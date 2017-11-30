import newspaper
from newspaper import Article
from make_comparison import Comparison

class WebScraper():

	def __init__(self):
	
		# List of websites to scrape for article information
		self.websites = ["http://cnn.com", "http://www.huffingtonpost.com", 
						 "http://www.breitbart.com", "http://www.foxnews.com",
						 "http://www.reuters.com", "http://occupydemocrats.com/"]
		
		# Holders for article URLs and entries for firebase database
		self.urls = []
		self.articles = []
		self.entries = {}
		
		# Sequence to get articles and scrape information
		self._getURLs()
		self._getDataInformatics()
		self.compare = Comparison(self.articles)

		
		
		
	def _getURLs(self):
	
		# Find all articles on each website and add URLs to list
		for website in self.websites:
			
			paper = newspaper.build(website, 'en')
			
			for article in paper.articles:
			
				self.urls.append(article.url)
				
		print("There were ", len(self.urls), " urls found.")
				
	
	def _getDataInformatics(self):
	
		# For each article URL, scape web and formulate database response
		for id, url in enumerate(self.urls, 1):
		
			if id == 3:
				break

			self._formulateDatabaseResponse(id, url)
			
			print('Formulating responses... %f percent complete' % (id * 100 / len(self.urls)))
			
			
	def _formulateDatabaseResponse(self, id, article):

		# Create a news article for each article URL
		news_article = Article(article)
		
		# Parse article for web scraping information
		news_article.download()
		news_article.parse()
		news_article.nlp()

		self.articles.append(news_article)



if __name__ == "__main__":

    WebScraper()
		
	
		
			
		
			
	
		
