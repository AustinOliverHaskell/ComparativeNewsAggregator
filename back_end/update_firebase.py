from firebase import firebase
from firebase_admin import db

class UpdateFirebase():

	def __init__(self, articles):
	
		# entries is a list of lists
		self.entries = []
		self.keyBois = []
		
		self.rawComparisons = articles[0:100]
		self.articleHashes = []
		self.comparisonHashes = []

		self._makeJSON(articles)
		
		
		self._fillKeyBois(articles)
		
		# Connection to Firebase
		self.database = firebase.FirebaseApplication("https://newsapp-5d5a8.firebaseio.com/")

		# Check entry to see if it fits criteria
		self._checkParams()
		
		# Push entry to database and update keywords
		self._pushEntries()

	def _fillKeyBois(self, articles):
		for comparison in articles:
			for keyBoi in comparison.getMatchingKeywords():
				if keyBoi not in self.keyBois: self.keyBois.append(keyBoi)

	def _makeJSON(self, articles):
	
		for comparison in articles:
			articleList =[]
			for article in [comparison.getFirstArticle(), comparison.getSecondArticle()]:
				articleList.append({
                                    "URL":article.url,
                                    "Title":article.title,
                                    "Text":article.text,
                                    "Author":article.authors,
                                    "Leaning":{"Center" : 0, "Center Left" : 0, "Center Right": 0, "Left" : 0, "Right":0},
                                    "Keywords":article.keywords,
                                    "Rating":{
                                    "UP":0,
                                    "DOWN":0},
                                    "Comparisons":[]})
                                    
			self.entries.append(articleList)

	def _checkParams(self):
	
		if type(self.entries) != list:
			
			raise ValueError("The entry must be a list of lists containing two comparison articles in order to post to Firebase")
			
		if len(self.entries) == 0:
			
			raise ValueError("The list of lists is empty. Nothing can be posted to the Firebase")
			
	def _pushEntries(self):
		
		for comparison in self.entries:
			del self.articleHashes[:]
			self.articleHashes = []
			for article in comparison:
				
				# Post article to database
				self.articleHashes.append(self.database.post("Articles", article)["name"])
				
			# Update the comparisons for each article
			self._updateComparisons()
		
		self._updateKeyBois()
		self._updateKeywords()	

	def _updateComparisons(self):
	
		# Note comparison for each key	
		self.comparisonHashes.append(self.database.post("Comparisons", self.articleHashes)["name"])
	
	def _updateKeyBois(self):
	
		self.database.patch("", {"Keybois": self.keyBois})
	
	def _updateKeywords(self):
		print(len(self.comparisonHashes))
		print(len(self.rawComparisons))

		for hash_id, comparison in enumerate(self.rawComparisons, start = 0):
	
			keywords = comparison.getMatchingKeywords()
		
			for keyword in keywords:
		
				if self.database.get("Keywords/%s" % keyword, None) is None:
				
					self.database.patch("Keywords", {keyword : [self.comparisonHashes[hash_id]]})
				
				else:
			
					comparison_list = self.database.get("Keywords/%s" % keyword, None)
				
					comparison_list.append(self.comparisonHashes[hash_id])
				
					self.database.patch("Keywords", {keyword: comparison_list})
				
				  
				
			
		
		
