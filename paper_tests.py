import unittest
from writing_set.paper import Sheet

class PaperTests(unittest.TestCase):

	def setUp(self):
		self.string1 = "Hello you"
		self.string2 = "Bilbo Baggins"
		self.combinedString = self.string1 + self.string2
		self.sheet = Sheet()
		
	def test_whenWritingString_contentIsInput(self):
	
		self.sheet.write_down(self.string1)
	
		self.assertEqual( self.sheet.get_content(), self.string1)
		
	def test_whenWritingTwice_secondStringAppendedToFirst(self):
	    
		self.sheet.write_down(self.string1)
		self.sheet.write_down(self.string2)
		
		self.assertEqual( self.sheet.get_content(), self.combinedString)
		
		
if __name__ == "__main__":
	unittest.main()
