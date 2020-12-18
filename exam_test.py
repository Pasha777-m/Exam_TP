import unittest as ut
import exam_Minyuk as pt

class CalcTest(ut.TestCase):
    def setUp(self):
        self.mk=pt.fac(n)
    def test_usage(self):
        self.assertEqual(self.mk.fac(n),120)

if __name__ == "__main__":
    import xmlrunner
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    ut.main(testRunner=runner)
    ut.main()
