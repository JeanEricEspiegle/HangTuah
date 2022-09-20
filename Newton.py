import requests
import json
import time
import logging
from bs4 import BeautifulSoup


class newton():
	s = requests.Session()
	cookies = []
	headers = []
	def login(self, hostname, hostpw):
		data = {
		    'username':hostname ,
		    'password': hostpw,
		}
		response = self.s.post('https://kiosk.nplay11.com/api/admin/login', data=data)
		self.cookies = response.cookies
		self.headers = response.headers
		#print(response.json())

	def getBalance(self):
		response = self.s.get('https://kiosk.nplay11.com/api/admin/balance')
		#print(response.json())

	def create_player(self,hostname,playername):
		data = {
		    'playername': hostname+playername,
		    'adminname': hostname,
		    'kioskname': hostname,
		    'languagecode': 'EN',
		}
		response = self.s.post('https://kiosk.nplay11.com/api/player/create', data=data)
		#print(response.json())

	def search_player(self, hostname, playername):
		data = {
		    'playername': hostname+playername,
		}

		response = self.s.post('https://kiosk.nplay11.com/api/player/info', data=data)
		#print(response.json())

	def deposit(self):
		data = {
		    'playername': 'NNK1R4801A1',
		    'adminname': 'NNK1R4801',
		    'amount': '10',
		}

		response = self.s.post('https://kiosk.nplay11.com/api/player/deposit', data=data)
		print(response.json())

	def withdraw(self):
		data = {
		    'playername': 'NNK1R4801A1',
		    'adminname': 'NNK1R4801',
		    'amount': '10',
		}

		response = self.s.post('https://kiosk.nplay11.com/api/player/withdraw', data=data)
		print(response.json())


man = newton()
man.login('NNK1R4801','Rose8888')
man.getBalance()
#man.create_player('NNK1R4801','A3')
man.search_player('NNK1R4801','A3')
man.deposit()
man.withdraw()