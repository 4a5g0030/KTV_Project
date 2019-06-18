import unittest
from Ktv import Comparison_ktv

class KtvTestCase(unittest.TestCase):

    def setUp(self):
        self.Ktv = Comparison_ktv()

    def test_5_20_3_10(self):
        self.Ktv.set_data(5, 20, 3, 10)
        people, room = self.Ktv.Calculation()
        self.assertEqual(5368, people)
        self.assertEqual(4059, room)
    
    def test_1_11_4_5(self):
        self.Ktv.set_data(1, 11, 4, 5)
        people, room = self.Ktv.Calculation()
        self.assertEqual(1914, people)
        self.assertEqual(2915, room)
    
    def test_1_11_8_5(self):
        self.Ktv.set_data(1, 11, 8, 5)
        people, room = self.Ktv.Calculation()
        self.assertEqual(3069, people)
        self.assertEqual(5071, room)
    
    def test_1_16_8_5(self):
        self.Ktv.set_data(1, 16, 8, 5)
        people, room = self.Ktv.Calculation()
        self.assertEqual(3564, people)
        self.assertEqual(5071, room)

    def test_6_18_6_20(self):
        self.Ktv.set_data(6, 18, 6, 20)
        people, room = self.Ktv.Calculation()
        self.assertEqual(17556, people)
        self.assertEqual(11352, room)

    def test_6_18_7_20(self):
        self.Ktv.set_data(6, 18, 7, 20)
        people, room = self.Ktv.Calculation()
        self.assertEqual(19756, people)
        self.assertEqual(12738, room)

    def test_5_16_8_3(self):
        self.Ktv.set_data(5, 16, 8, 3)
        people, room = self.Ktv.Calculation()
        self.assertEqual(2633, people)
        self.assertEqual(3535, room)

    def test_1_23_5_7(self):
        self.Ktv.set_data(1, 23, 5, 7)
        people, room = self.Ktv.Calculation()
        self.assertEqual(3065, people)
        self.assertEqual(4528, room)

    def test_5_23_2_11(self):
        self.Ktv.set_data(5, 23, 2, 11)
        people, room = self.Ktv.Calculation()
        self.assertEqual(5542, people)
        self.assertEqual(3364, room)

    def test_6_0_2_11(self):
        self.Ktv.set_data(6, 0, 2, 11)
        people, room = self.Ktv.Calculation()
        self.assertEqual(5542, people)
        self.assertEqual(3364, room)

    def test_time_error(self):
        self.Ktv.set_data(1, 9, 10, 10)
        people, room = self.Ktv.Calculation()
        self.assertEqual("輸入時間為打烊時間", people)
        self.assertEqual("輸入時間為打烊時間", room)