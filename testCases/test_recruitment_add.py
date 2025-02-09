import pytest
from pageObject.LoginPage import loginpage
from pageObject.AddRecruit_Page import AddRecruitment
from utilities.readProperties import Readconfig
from utilities.Logger import LogGenerator
import time

class Test_Add_Recruitment:
    url = Readconfig.geturl()
    username = Readconfig.getusername()
    password = Readconfig.getpassword()
    log = LogGenerator.loggen()

    def test_addRecruitment_009(self,setup):
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.log.info("test_addRecruitment_009 is started")
        self.log.info("Browser is openning")
        self.driver.get(self.url)
        self.log.info("Going to url -->"+self.url)
        self.lp = loginpage(self.driver)
        self.lp.Enter_UserName(self.username)
        self.log.info("Enter Username-->"+self.username)
        self.lp.Enter_Password(self.password)
        self.log.info("Enter Password -->"+self.password)
        self.lp.Click_Login()
        self.log.info("Click on login Button")
        self.ar = AddRecruitment(self.driver)
        self.ar.Click_Recruitment()
        self.log.info("CLick on Recruitment Button")
        self.ar.Click_AddRecruit()
        self.log.info("Cick on Add Button")
        self.ar.Enter_FirstName("Smith")
        self.log.info("Enter FirstName --> Smith")
        self.ar.Enter_MiddleName("R")
        self.log.info("Enter Middlename --> R")
        self.ar.Enter_LastName("L")
        self.log.info("Enter Lastname --> L")
        self.ar.Click_DropDown("Software Engineer")
        self.log.info("Select option in job vaccancies --> Software Engineer")
        self.ar.Enter_Email("smith1233@gmail.com")
        self.log.info("Enter Email --> smith1233@gmail.com")
        time.sleep(4)
        self.ar.Click_Save()
        self.log.info("Click Save Button")
        if self.ar.RecruitmentStatus() == True:
            time.sleep(5)
            self.driver.save_screenshot(
                "D:\\Credence\\Automation Testing Selenium Python Tushar Sir\\Practice OrangeHrm\\Screenshot\\test_addRecruitment_009_pass.png")
            self.log.info("Save Screenshot")
            self.lp.Click_MenuButton()
            self.log.info("Click on Menu buttom")
            self.lp.Click_Logout()
            self.log.info("Click on Logout")
            assert True
            self.log.info("test_addRecruitment_009 is Passed")

        else:
            self.driver.save_screenshot(
                "D:\\Credence\\Automation Testing Selenium Python Tushar Sir\\Practice OrangeHrm\\Screenshot\\test_addRecruitment_009_fail.png"
                )
            self.log.info("Save Screenshot")
            self.log.info("test_addRecruitment_009 is Failed")
            assert False
        self.driver.close()
        self.log.info("test_addRecruitment_009 is Completed")

