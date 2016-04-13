import unittest

from ddt import ddt,data,unpack
from selenium import webdriver
from Page.LoginPage import LoginPage
from Page.HomePage import HomePage
from BaseTestCases.BaseTestCase import BaseTestCase
from DataSource.read_excel import read_excel

@ddt
class LoginTest(BaseTestCase):


    @data(*read_excel.get_data_from_excel('D:/Selenium-Python/ACE_Automation/Data/login_data.xlsx','login'))
    @unpack
    def test_login_with_valid_credentials(self,Username,Password,LoginName):
       LoginPage.login(self,Username,Password)
       self.assertEqual(LoginName,HomePage.get_login_name(self))
       print(HomePage.get_login_name(self))




if __name__ == '__main__':
    unittest.main()
