import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


class Scrapper: 
    def __init__(self):
        options = webdriver.ChromeOptions()
        # options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path="./chromedriver_win32/chromedriver.exe", options=options)
        # self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        
    def get_business(self, url):
        self.driver.get(url)
        
        height = self.driver.execute_script('return document.querySelectorAll(".m6QErb.DxyBCb.kA9KIf.dS8AEf.ecceSd")[1].scrollHeight')
        while True:   
            self.driver.execute_script(f'document.querySelectorAll(".m6QErb.DxyBCb.kA9KIf.dS8AEf.ecceSd")[1].scrollTo(0, {height});')
            time.sleep(5)
            new_height = self.driver.execute_script('return document.querySelectorAll(".m6QErb.DxyBCb.kA9KIf.dS8AEf.ecceSd")[1].scrollHeight')
            if new_height == height:
                self.get_data()
                break
            height = new_height
        


    def get_data(self):
        elements = self.driver.find_elements_by_class_name("hfpxzc")
        links = [el.get_attribute('href') for el in elements]
        
        for link in links:
            self.driver.get(link)
        
        
            data = self.driver.find_elements(By.CSS_SELECTOR, ".Io6YTe.fontBodyMedium")
            text = [el.get_attribute('innerHTML') for el in data]

            business_name = self.driver.find_element_by_class_name("DUwDvf").text
            business_address = text[0]
            business_phone = ''
            business_email = ''
        
            for i in range(len(text)):
                if (text[i][0]=="+"):
                    business_phone = text[i]
                if("@" in text[i]):
                    business_email = text[i]

            print(business_name, business_address, business_phone, business_email)

        
query = "restaurantes valencia"
url = "https://www.google.es/maps/search/"+query.replace(" ", "+")+"/"

gmaps = Scrapper()
gmaps.get_business(url)
# gmaps.full_scroll(url)

