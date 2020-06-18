import unittest
from score_management_system import ScoreManagementSystem
from unittest.mock import Mock
from unittest.mock import patch
from unittest.mock import mock_open


class TestScoreManagementSystem(unittest.TestCase):

    def setUp(self):
        self.m_open1 = mock_open(read_data= "1,강호민,85,90,95\n")
        self.m_open2 = mock_open(read_data= "1,강호민,85,90,95\n2,김광호,80,70,60\n")
        self.m_open3 = mock_open(read_data= "1,강호민,85,90,95\n2,김광호,80,70,60\n14,이주경,70,70,80\n")


    def test_constructor(self):
        sms = ScoreManagementSystem()
        self.assertIsNotNone(sms)


    def test_read_1(self):

        with patch("score_management_system.open",self.m_open1):
            sms = ScoreManagementSystem()
            self.assertEqual(1,sms.read('score.csv'))

        self.m_open1.assert_called_with('score.csv', 'rt', encoding='utf-8')

    def test_read_2(self):

        with patch("score_management_system.open",self.m_open2):
            sms = ScoreManagementSystem()
            self.assertEqual(2,sms.read('score.csv'))

        self.m_open2.assert_called_with('score.csv', 'rt', encoding='utf-8')

    def test_read_3(self):

        with patch("score_management_system.open",self.m_open3):
            sms = ScoreManagementSystem()
            self.assertEqual(3,sms.read('score.csv'))

        self.m_open3.assert_called_with('score.csv', 'rt', encoding='utf-8')

    def test_sort_1(self):

        with patch("score_management_system.open",self.m_open1):
            sms = ScoreManagementSystem()
            sms.read('score.csv')

            result = sms.sort(order_key="register",order_way="asc")
            self.assertEqual('1,강호민,85,90,95,270,90,1',result)

    def test_sort_2(self):

        with patch("score_management_system.open",self.m_open2):
            sms = ScoreManagementSystem()
            sms.read('score.csv')

            result = sms.sort(order_key="register",order_way="asc")
            self.assertEqual('1,강호민,85,90,95,270,90,1\n2,김광호,80,70,60,210,70,2',result)

    def test_sort_3(self):

        with patch("score_management_system.open",self.m_open2):
            sms = ScoreManagementSystem()
            sms.read('score.csv')

            result = sms.sort(order_key="register",order_way="des")
            self.assertEqual('2,김광호,80,70,60,210,70,2\n1,강호민,85,90,95,270,90,1',result)

    def test_sort_4(self):

        with patch("score_management_system.open",self.m_open3):
            sms = ScoreManagementSystem()
            sms.read('score.csv')

            result = sms.sort(order_key="register",order_way="des")
            self.assertEqual('14,이주경,70,70,80,220,73.33,3\n2,김광호,80,70,60,210,70,2\n1,강호민,85,90,95,270,90,1',result)

    def test_sort_5(self):

        with patch("score_management_system.open",self.m_open3):
            sms = ScoreManagementSystem()
            sms.read('score.csv')

            result = sms.sort(order_key="rank",order_way="asc")
            self.assertEqual('1,강호민,85,90,95,270,90,1\n14,이주경,70,70,80,220,73.33,2\n2,김광호,80,70,60,210,70,3',result)

    def test_sort_6(self):

        with patch("score_management_system.open",self.m_open3):
            sms = ScoreManagementSystem()
            sms.read('score.csv')

            result = sms.sort("rank","asc")
            self.assertEqual('1,강호민,85,90,95,270,90,1\n14,이주경,70,70,80,220,73.33,2\n2,김광호,80,70,60,210,70,3',result)

    def test_sort_7(self):

        with patch("score_management_system.open",self.m_open3):
            sms = ScoreManagementSystem()
            sms.read('score.csv')

            result = sms.sort("rank","des")
            self.assertEqual('2,김광호,80,70,60,210,70,3\n14,이주경,70,70,80,220,73.33,2\n1,강호민,85,90,95,270,90,1',result)


if __name__ == "__main__":
    unittest.main()


