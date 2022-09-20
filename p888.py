import requests
import json
import time
import logging
from bs4 import BeautifulSoup

class pussy888():
	#logging.basicConfig(level=logging.DEBUG)
	s = requests.Session()	

	def login(self):
		self.s.get('http://kiosk.pussy888.com/handler/LoginHandler.ashx?action=login&userName=68PSY243&passWd=Rose8888&country=N%2FA&city=N%2FA')

	def getCurrentBalance(self):
		response2 = self.s.post('http://kiosk.pussy888.com/handler/datahandler/CurrentBalance.ashx?action=GetCurrScore&ts=903250')
		data2 = response2.json()
		#print(data2)

	def check_login(self):
		response3 = self.s.post('http://kiosk.pussy888.com/handler/CheckUsers.ashx?action=CheckLogin&ts=3028336')
		data3 = response3.json()
		#print(data3)

	def logout(self):
		self.s.close()

	def set_score(self, account, amount):
		payload = 'http://kiosk.pussy888.com/handler/userhandler/UserScore.ashx?action=setAccountScore&scoreNum='+amount+'&MaxNum=999.00&userName='+account+'&ts=8208462'
		response3 = self.s.post(payload)
		data3 = response3.json()
		#print(data3)

	def add_user(self,amount, name, phone):
		password = 'Aaa123'
		
		response4 = self.s.get('http://kiosk.pussy888.com/english/AddAccount.aspx?sname=68psy243&operate=addAccount&rid=tYLzlx3zEz')
		soup = BeautifulSoup(response4.text, 'html.parser')
		playerName = soup.find(id='s_playerID').text
		print(playerName)
		payload = 'http://kiosk.pussy888.com/handler/userhandler/Users.ashx?action=addUser&agent=68psy243&userName='+playerName+'&PassWd='+password+'&Name='+name+'&Tel='+ phone +'&Memo=&UserType=1&ts=3942473&scoreNum=0&MaxNum=1000.00'
		response5 = self.s.post(payload)
		data = response5.json()
		#print (data)
		self.getUserDetail(playerName)

	def getUserDetail(self, playerName):
		payload = 'http://kiosk.pussy888.com/handler/userhandler/Users.ashx?action=getSearchUserInfo&userName='+playerName+'&ts=1097137'
		response = self.s.post(payload)
		data = response.json()
		print(data)


game = pussy888()
game.login()
game.getCurrentBalance()
game.check_login()
game.set_score('my618159161', '10')
game.add_user('0', 'John','1234567')
game.logout()