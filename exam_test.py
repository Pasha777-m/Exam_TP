import unittest as ut
import random
import exam_Minyuk as pt
import numpy as np

class CalcTest(ut.TestCase):
    def setUp(self):
        self.mk=pt.MyClass()
    def test_add(self):
        self.assertEqual(self.mk.Progression(1,2),3)

if __name__ == "__main__":
    import xmlrunner
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    ut.main(testRunner=runner)
    ut.main()
