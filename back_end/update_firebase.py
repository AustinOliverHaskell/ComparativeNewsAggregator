from firebase import firebase
from firebase_admin import db

class UpdateFirebase():

	def __init__(self, articles):
	
		# entries is a list of lists
		self.entries = []
		self._makeJSON(articles)

		# Check entry to see if it fits criteria
		self._checkParams()
	
		# Connection to Firebase
		self.database = firebase.FirebaseApplication("https://newsapp-5d5a8.firebaseio.com/")
		
		# Push entry to database and update keywords
		self._pushEntries()
		
	def _makeJSON(self, articles):
		for comparison in articles:
			articleList = []
			for article in comparison:
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
		print(self.entries)

		print(self.entries)
	def _checkParams(self):
	
		if type(self.entries) != list:
			
			raise ValueError("The entry must be a list of lists containing two comparison articles in order to post to Firebase")
			
		if len(self.entries) == 0:
			
			raise ValueError("The list of lists is empty. Nothing can be posted to the Firebase")
			
	def _pushEntries(self):
		
		for comparison in self.entries:
					
			# Holds two hash keys for articles in Firebase
			comparison_hash_keys = []
		
			for article in comparison:
				
				# Post article to database
				comparison_hash_keys.append(self.database.post("Articles", article)["name"])
				
			# Update the comparisons for each article
			self._updateComparisons(comparison_hash_keys)

	def _updateComparisons(self, comparison_hash_keys):
	
		# Note comparison for each key	
		comparison_id = self.database.post("Comparisons", comparison_hash_keys)
			
		for article in comparison_hash_key:
		
			# Get and update comparison list for each article
			article_id = self.database.get("Articles/%s/Comparisons" % article, None)
			
			# Update comparison list with new comparison id
			article_id.append(comparison_id)
			
			# Update firebase with new comparison added to list
			self.database.patch("Articles/%s/Comparisons" % article, article_id)	
			
	
		
		
					