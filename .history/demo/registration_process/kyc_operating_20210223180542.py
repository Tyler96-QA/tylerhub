from KYC_method import kyc_approve
from selenium import webdriver
import unittest


#实例化对象
kyc=kyc_approve()

class kyc_actions(unittest.TestCase):

    def setUp(self):
        kyc.browsertype()

    def test(self):
        kyc.login_cp('CN','tyler.tang@qq.com','Tl123456')


if __name__=='__main__':
    unittest.main()