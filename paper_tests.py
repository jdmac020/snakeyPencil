import unittest
from writing_set.paper import Sheet

class PaperTests(unittest.TestCase):

	def setUp(self):
		pass
		
	def test_whenWritingString_contentIsInput(self):
	
		testString = "Hello you"
		testPaper = Sheet()
		
		testPaper.write_down(testString)
	
		self.assertEqual( testPaper.get_content(), testString)
		
	def test_whenWritingTwice_secondStringAppendedToFirst(self):
	    
		string1 = "Hello you"
		string2 = " Bilbo Baggins"
		testPaper = Sheet()
		
		testPaper.write_down(string1)
		testPaper.write_down(string2)
		
		self.assertEqual( testPaper.get_content(), string1+string2)
		
		
if __name__ == "__main__":
	unittest.main()
