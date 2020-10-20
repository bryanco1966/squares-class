import unittest
from polygon import Polygon
class TestPolygon(unittest.TestCase):

    def test_init(self):
        result = Polygon(3,5)
        self.assertEqual(result, Polygon(3,5))

    def test_count_edges(self):
        result = Polygon(4,6).count_edges
        self.assertEqual(result, 4)





unittest.main()
