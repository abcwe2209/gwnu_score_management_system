import unittest
from score_management_system import ScoreManagementSystem
from unittest.mock import Mock
from unittest.mock import patch
from unittest.mock import mock_open


class TestScoreManagementSystem(unittest.TestCase):

    def setUp(self):
        self.m_open1 = mock_open(read_data= "1,강호민,85,90,95\n")


    def test_constructor(self):
        sms = ScoreManagementSystem()
        self.assertIsNotNone(sms)


    def test_read_1(self):

        with patch("score_management_system.open",self.m_open1):
            sms = ScoreManagementSystem()
            self.assertEqual(1,sms.read('score.csv'))





if __name__ == "__main__":
    unittest.main()


