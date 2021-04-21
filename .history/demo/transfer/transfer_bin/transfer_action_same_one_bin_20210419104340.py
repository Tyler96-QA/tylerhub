import os
import sys
import unittest

import ddt
from BeautifulReport import BeautifulReport

path_public=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))+r'\public'
sys.path.append(path_public)
path_transfer=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(path_transfer+r'\transfer_location')
from about_data import exceldata
from location_transfer_same_one import location_of_transfer


transfer=location_of_transfer()
e=exceldata()
excelpath=path_transfer+r'\test_data\transfer_same_one.xlsx'
print(excelpath)
rows=e.openexcel(excelpath,'Sheet1')
testdata=e.dict_data()
print(testdata)

@ddt.ddt
class transfertion(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        transfer.broswertype()
        transfer.get_url('tyler.tang','Tl123456')

    @ddt.data(*testdata)
    def test_transfer(self,data):
        print(data['主账号'])
        #判断主账号，交易账户是否满足转账条件
        #transfer.is_satisfy_transfer(int(float(data['主账号'])),int(float(data['转出交易账号'])),int(float(data['转入交易账号'])))
        transfer.transfer_in_cp('lemon.lin@newtype.io','Tl123456',1000003759,67200977,63200106,666)


  
if __name__=='__main__':
    unittest.main()