from selenium import webdriver   # for webdriver
from selenium.webdriver.support.ui import WebDriverWait  # for implicit and explict waits
from selenium.webdriver.chrome.options import Options  # for suppressing the browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

class jokerManager():

	option = webdriver.ChromeOptions()
	option.add_argument('headless')
	driver = webdriver.Chrome('C:/Users/jee30/Desktop/HangTuah/chromedriver',options=option)
	
	def login(self,username, password):
		username = "68J0243"
		password ="Rose8888"

		self.driver.get('https://www.awebo68.net/Account')
		print("Page title was '{}'".format(self.driver.title))

		uname = self.driver.find_element(By.ID,"Username")
		uname.send_keys(username)

		pword = self.driver.find_element(By.ID,"Password")
		pword.send_keys(password)

		submit = self.driver.find_element(By.ID,"btnLogin")
		submit.click()

		WebDriverWait(driver=self.driver, timeout=10).until(
		    lambda x: x.execute_script("return document.readyState === 'complete'")
		)

		error_message = "Incorrect username or password."
		errors = self.driver.find_elements(By.CLASS_NAME,"flash-error")
		if any(error_message in e.text for e in errors):
		    print("[!] Login failed")
		else:
		    print("[+] Login successful")
		print("Page title was '{}'".format(self.driver.title))

	def newMemberPage(self):
		wait = WebDriverWait(self.driver, 10)
		self.driver.find_element(By.ID,"hamburger-icon").click()
		time.sleep(2)
		wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/aside/nav/section[1]/ul/li[1]/a'))).click()
		#self.driver.find_element(By.XPATH,'/html/body/aside/nav/section[1]/ul/li[1]/a').click()
		time.sleep(2)
		self.driver.find_element(By.XPATH,'/html/body/aside/nav/section[1]/ul/li[1]/ul/li[2]/a').click()
		WebDriverWait(driver=self.driver, timeout=20).until(
		    lambda x: x.execute_script("return document.readyState === 'complete'")
		)
		time.sleep(2)
		strUrl = self.driver.current_url;
		print(strUrl)

	def addMember(self,password, amount):
		wait = WebDriverWait(self.driver, 10)
		wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/main/div/div/div[2]/form/div/div/div/div[2]/table[1]/tbody/tr[1]/td[2]/div/div[1]/div[1]/div/a'))).click()
		#self.driver.find_element(By.XPATH,'/html/body/div[1]/main/div/div/div[2]/form/div/div/div/div[2]/table[1]/tbody/tr[1]/td[2]/div/div[1]/div[1]/div/a').click()
		time.sleep(1)

		pw = self.driver.find_element(By.XPATH,'/html/body/div[1]/main/div/div/div[2]/form/div/div/div/div[2]/table[1]/tbody/tr[1]/td[4]/div/input')
		pw.send_keys(password)
		
		amt = self.driver.find_element(By.XPATH,'/html/body/div[1]/main/div/div/div[2]/form/div/div/div/div[2]/table[1]/tbody/tr[7]/td[2]/input')
		amt.send_keys(amount)

		ID = self.driver.find_element(By.XPATH,'/html/body/div[1]/main/div/div/div[2]/form/div/div/div/div[2]/table[1]/tbody/tr[1]/td[2]/div/div[1]/div[1]/input')
		ID = ID.get_attribute("value")

		self.driver.find_element(By.XPATH,'/html/body/div[1]/main/div/div/div[2]/form/div/div/div/div[2]/div[4]/input[1]').click()		

		return ID

	def quit(self):
		self.driver.quit()

	def hostMoney(self):
		wait = WebDriverWait(self.driver, 10)
		wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/header/section[2]/span'))).click()
		wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/div[1]/main/div/div/div[1]/div/div[1]/div[1]/div/div[5]/div[2]/div[2]/table/tbody/tr/td/span[1]'))).click()
		time.sleep(1)
		money = self.driver.find_element(By.XPATH,'/html/body/div[1]/main/div/div/div[1]/div/div[1]/div[1]/div/div[5]/div[2]/div[2]/table/tbody/tr/td/strong')
		money2 = money.get_attribute("textContent")
		return money2

	def search(self,ID):
		wait = WebDriverWait(self.driver, 10)
		self.driver.find_element(By.ID,"hamburger-icon").click()
		wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/aside/nav/section[1]/ul/li[1]/a'))).click()
		wait.until(EC.element_to_be_clickable((By.XPATH,'/html/body/aside/nav/section[1]/ul/li[1]/ul/li[3]/a'))).click()
		time.sleep(2)
		username = self.driver.find_element(By.XPATH,'/html/body/div[1]/main/div/div[1]/div[2]/div/form/div/div[1]/div/input')
		time.sleep(1)
		username.send_keys(ID)
		wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/main/div/div[1]/div[2]/div/form/div/div[4]/input'))).click()
		WebDriverWait(driver=self.driver, timeout=20).until(
		    lambda x: x.execute_script("return document.readyState === 'complete'")
		)
		freeKredit = self.driver.find_element(By.XPATH,'/html/body/div[1]/main/div/div[1]/div[3]/div[2]/div/div[4]/table/tbody/tr/td[7]').text
		Kredit = self.driver.find_element(By.XPATH,'/html/body/div[1]/main/div/div[1]/div[3]/div[2]/div/div[4]/table/tbody/tr/td[6]/a/span').text
		return Kredit,freeKredit


class getClass():
	username = "68J0243"
	password ="Rose8888"
	manager = jokerManager()
	manager.login(username,password)
	def createMember(self, amount):
		self.manager.newMemberPage()
		ID = self.manager.addMember("Aaaa1234", amount)
		return ID, amount

	def getUserDetails(self):
		credit,freecredit = self.manager.search(1538521089)
		return credit, freecredit


	def getHostMoney(self):
		money = self.manager.hostMoney()
		return money
	def quit():
		self.manager.quit()



access = getClass()
ID, amount = access.createMember(10)
credit,freecredit = access.getUserDetails()
money = access.getHostMoney()
print("ID and Amount: ",ID,", ",amount)
print("User Money: ",credit,", ", freecredit)
print("Host Funds: ",money)