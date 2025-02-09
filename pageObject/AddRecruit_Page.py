import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException as Ec
from selenium.webdriver.support import expected_conditions as EC


class AddRecruitment:
    Click_Recruitment_XPATH = (By.XPATH,"//span[@class='oxd-text oxd-text--span oxd-main-menu-item--name'][normalize-space()='Recruitment']")
    Click_AddRecruit_XPATH = (By.XPATH,"//button[normalize-space()='Add']")
    Text_FirstName_XPATH = (By.XPATH,"//input[@placeholder='First Name']")
    Text_MiddleName_XPATH = (By.XPATH,"//input[@placeholder='Middle Name']")
    Text_LastName_XPATH = (By.XPATH,"//input[@placeholder='Last Name']")
    DropDown_Vacancy_XPATH = (By.CSS_SELECTOR,"div.oxd-select-text.oxd-select-text--active")
    DropDown_Option_XPATH = (By.XPATH,"//div[@class='oxd-select-text-input']")
    Text_Email_XPATH = (By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/form[1]/div[3]/div[1]/div[1]/div[1]/div[2]/input[1]")
    Click_Save_XPATH = (By.XPATH,"//button[@type='submit']")
    RecruitStatus_XPATH = (By.XPATH,"//p[@class='oxd-text oxd-text--p oxd-text--subtitle-2']")

    def __init__(self,driver):
        self.driver = driver

    def Click_Recruitment(self):
        self.driver.find_element(*AddRecruitment.Click_Recruitment_XPATH).click()

    def Click_AddRecruit(self):
        self.driver.find_element(*AddRecruitment.Click_AddRecruit_XPATH).click()

    def Enter_FirstName(self,firstname):
        self.driver.find_element(*AddRecruitment.Text_FirstName_XPATH).send_keys(firstname)

    def Enter_MiddleName(self,middlename):
        self.driver.find_element(*AddRecruitment.Text_MiddleName_XPATH).send_keys(middlename)

    def Enter_LastName(self,lastname):
        self.driver.find_element(*AddRecruitment.Text_LastName_XPATH).send_keys(lastname)

    def Click_DropDown(self,option_text):
        wait = WebDriverWait(self.driver,10)

        option = self.driver.find_element(By.XPATH,"//div[contains(@class, 'oxd-select-text-input')]")
        more = option.find_elements(By.XPATH,"//div[contains(@class, 'oxd-select-text-input')]")
        for o in more:
            print(o.text)




    def Enter_Email(self,email):
        self.driver.find_element(*AddRecruitment.Text_Email_XPATH).send_keys(email)

    def Click_Save(self):
        self.driver.find_element(*AddRecruitment.Click_Save_XPATH).click()

    def RecruitmentStatus(self):
        self.driver.implicitly_wait(10)
        try:
            self.driver.find_element(*AddRecruitment.RecruitStatus_XPATH)
            return True
        except Ec:
            return False



