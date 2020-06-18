import unittest
from score import Score


class TestScore(unittest.TestCase):

    def setUp(self):
        self.my_score1 = Score("1,강호민,85,90,95\n")
        self.my_score2 = Score("2,김광호,80,70,60\n")
        self.my_score3 = Score("14,이주경,70,70,80\n")

    def test_constructor(self):
        self.assertIsNotNone(self.my_score1)
        self.assertIsNotNone(self.my_score2)
        self.assertIsNotNone(self.my_score3)

    def test_no_1(self):
        self.assertEqual(1,self.my_score1.no)

    def test_no_2(self):
        self.assertEqual(2,self.my_score2.no)

    def test_no_3(self):
        self.assertEqual(14,self.my_score3.no)


    def test_name_1(self):
        self.assertEqual('강호민',self.my_score1.name)

    def test_name_2(self):
        self.assertEqual('김광호',self.my_score2.name)

    def test_name_3(self):
        self.assertEqual('이주경',self.my_score3.name)
        #85,90,95
    def test_score_1(self):
        self.assertEqual(85,self.my_score1.kor)
        self.assertEqual(90,self.my_score1.eng)
        self.assertEqual(95,self.my_score1.math)

    def test_score_2(self):
        self.assertEqual(80,self.my_score2.kor)
        self.assertEqual(70,self.my_score2.eng)
        self.assertEqual(60,self.my_score2.math)
    
    def test_score_3(self):
        self.assertEqual(70,self.my_score3.kor)
        self.assertEqual(70,self.my_score3.eng)
        self.assertEqual(80,self.my_score3.math)
     
    def test_sum_1(self):
        self.assertEqual(270,self.my_score1.sum)

    def test_sum_2(self):
        self.assertEqual(210,self.my_score2.sum)

    def test_sum_3(self):
        self.assertEqual(220,self.my_score3.sum)
       
    def test_avg_1(self):
        self.assertEqual(90,self.my_score1.avg)

    def test_avg_2(self):
        self.assertEqual(70,self.my_score2.avg)

    def test_avg_3(self):
        self.assertEqual(73.33,self.my_score3.avg)
        


if __name__ == "__main__":
    unittest.main()