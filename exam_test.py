import unittest as ut
import exam_Minyuk as pt

class CalcTest(ut.TestCase):
    def test_usage(self):
        n=5
        p = pt.fac(n)
        self.assertEqual(p,120)

if __name__ == "__main__":
    import xmlrunner
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    ut.main(testRunner=runner)
    ut.main()
