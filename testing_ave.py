import unittest
import ave

class testAve(unittest.TestCase):
	# Successful test
	def test_ave_1(self):
		self.assertEqual(ave.ave([4, -6, 0.3, 10]), 2.075)

	# Failed test
	def test_ave_2(self):
		self.assertEqual(ave.ave([]), 0)

	# Failed test
	def test_ave_3(self):
		self.assertEqual(ave.ave(["3", "2", "-12", 9, 7]), 1.8)

	if __name__ == '__main__':
		unittest.main()