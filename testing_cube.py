import unittest
import cube

class testCube(unittest.TestCase):
	# Successful test
	def test_cube_1(self):
		self.assertEqual(cube.cube(0.5), 0.125)

	# Failed test
	def test_cube_2(self):
		self.assertEqual(cube.cube(-4), 64)

	# Failed test
	def test_cube_3(self):
		self.assertEqual(cube.cube("4"), 64)

	if __name__ == '__main__':
		unittest.main()