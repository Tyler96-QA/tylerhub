import sys
import os
import time
path_demo=os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
path_public=path_demo+r'\public'
sys.path.append(path_public)
from browser_actions import Commonweb
from other_actions import public_method
from about_data import exceldata
from verification_code import time_used


comweb=Commonweb()

class pubfang():
    global driver

    def login_topup(self):

        comweb.display_click('css,div.rem-pwd-box>a')
