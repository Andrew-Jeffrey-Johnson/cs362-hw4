import unittest
import name

class testName(unittest.TestCase):
	# Successful test
	def test_name_1(self):
		self.assertEqual(name.name("Steve", "Johnson"), "Steve Johnson")

	# Failed test
	def test_name_2(self):
		self.assertEqual(name.name(), "")

	# Failed test
	def test_name_3(self):
		self.assertEqual(name.name("Josh", 9), "Josh 9")

	if __name__ == '__main__':
		unittest.main()