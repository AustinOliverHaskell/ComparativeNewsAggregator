from firebase import firebase
from firebase_admin import db

class UpdateFirebase():

	def __init__(self, entry):
	
		# Entry to be posted on firebase
		self.entry = entry
		
		# Check entry to see if it fits criteria
		self._checkParams()
	
		# Connection to Firebase
		self.database = firebase.FirebaseApplication("https://newsapp-5d5a8.firebaseio.com/")
		
		# Push entry to database and update keywords
		self._pushEntry()
		
	def _checkParams(self):
	
		if type(self.entry) != dict:
			
			raise ValueError("The entry must be a dictionary in order to post to Firebase")
		
	def _pushEntry(self):
	
		# Check to see if entry is already in database
		for entry in self.database.get("Articles", None).values():
		
			# If the entry is found in the database then notify user
			if self.entry == entry:
				print("Entry was already in database. Skipping entry")
				
			# If not found the database then post the article, reference id, and update keywords
			else:
				
				self.reference_id = self.database.post("Articles", self.entry, 
													   {'print': 'pretty'}, 
													   {'X_FANCY_HEADER': 'VERY FANCY'})
													   
				print('The reference id is: ', self.reference_id["name"])
				
				self._updateKeywords()
		
	def _updateKeywords(self):
	
		# Get Keywords of Articles
		self.keywords = self.entry["keywords"]
		
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
					