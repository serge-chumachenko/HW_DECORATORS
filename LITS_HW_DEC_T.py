import unittest
from decimal import*
from LITS_HW_DEC import summ,sub,mul,div,My_Zero_Division_Error,My_Type_Error

class SimpleTestCase(unittest.TestCase):
    def test_summ(self):
        self.assertEqual(summ(547.54327,451.45673),999.0)
        with self.assertRaises(My_Type_Error):summ([8],3)

    def test_sub(self):
        self.assertEqual(sub(2.477,1.478),0.9989999999999999)
        with self.assertRaises(My_Type_Error):sub(8,'5')

    def test_mul(self):
        self.assertEqual(mul(Decimal(2),Decimal(2.5)),5.0)
        with self.assertRaises(My_Type_Error):mul('2',2)

    def test_div(self):
        self.assertEqual(div(Decimal(5),Decimal(5)),1)
        with self.assertRaises(My_Type_Error):div(8,'312')
        with self.assertRaises(My_Zero_Division_Error):div(8, 0)


if __name__=='__main__':
    unittest.main()