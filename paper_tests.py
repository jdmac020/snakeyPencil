import unittest
from writing_set.paper import Sheet

class PaperTests(unittest.TestCase):

	def setUp(self):
		pass
		
	def test_paper_whenWritingString_contentIsInput(self):
	
		testString = "Hello you"
		testPaper = Sheet()
		
		testPaper.write_down(testString)
	
		self.assertEqual( testPaper.get_content(), testString)
		
if __name__ == "__main__":
	unittest.main()
