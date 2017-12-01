from firebase import firebase
from firebase_admin import db

class UpdateFirebase():

	def __init__(self, entries):
	
		# Entry is a list of lists
		self.entries = entries
		
		# Check entry to see if it fits criteria
		self._checkParams()
	
		# Connection to Firebase
		self.database = firebase.FirebaseApplication("https://newsapp-5d5a8.firebaseio.com/")
		
		# Push entry to database and update keywords
		self._pushEntries()
		
	def _checkParams(self):
	
		if type(self.entries) != list:
			
			raise ValueError("The entry must be a list of lists containing two comparison articles in order to post to Firebase")
			
		if self.entries.size() == 0:
			
			raise ValueError("The list of lists is empty. Nothing can be posted to the Firebase")
			
		
	def _pushEntries(self):
		
		for comparison in self.entries:
		
			# Hash key that references articles
			hash_keys = []
		
			for article in comparison:
			
				# Update keywords
				self._updateKeywords(article["Keywords"])
				
				# Append reference id to list for each comparison
				hash_keys.append(self.reference_id)
				
			# Update comparisons in article JSON and Comparison JSON
			self.updateComparisons(hash_keys)
							
	
	def _updateKeywords(self, keywords):
		
		# For each keyword in article,
		for keyword in self.keywords:
		
			# Check to see if keyword is in database
			if keyword in self.database.get("Keywords", None).keys():
				
				# If it is, then append reference id for article in list for that keyword
				list_articles_with_keyword = self.database.get("Articles/%s" % keyword, None)
				list_articles_with_keyword.append(self.reference_id)
				
				# Patch keyword with new updated list
				self.database.patch('/Keywords/%s/' % keyword, list_articles_with_keyword)
				
			else:
			
				# If keyword is not in database, add it and list with single reference id
				self.database.path('Keywords/%s/' % keyword, [self.reference_id]
				
	def _updateComparisons(self):
	
		
		
		
					