import requests
import json
import time
import logging
from bs4 import BeautifulSoup

class luckypalace():
	s = requests.Session()
	admin= 'JAS23MYRH10701'
	password = 'Rose8888'
	names =[]
	def login(self):
		data = {
		    'username': 'JAS23MYRH10701',
		    'password': 'Rose8888',
		}
		response = self.s.post('https://kiosk.pt-ka.com/api/admin/login?username='+self.admin+'&password='+self.password)

	def balance(self):
		response = self.s.get('https://kiosk.pt-ka.com/api/admin/balance')
		data = response.json()
		#print(data)

	def create_player(self):
		self.getPlayers()
		number = self.getAccountNumber()
		number = self.admin + number
		print(number)

		data = {
		    'playername': number,
		    'adminname': self.admin,
		    'kioskname': self.password,
		    'languagecode': 'EN',
		}

		response = self.s.post('https://kiosk.pt-ka.com/api/player/create?playername='+number+'&adminname='+self.admin+'&kioskname='+self.admin+'&languagecode=EN')
		data = response.json()
		print(data)

	def getPlayers(self):
		data = {
		    'timeperiod': 'all',
		    'startdate': '',
		    'enddate': '',
		    'viplevel': '',
		    'isfrozen': '0',
		    'entityname': '',
		    'page': '1',
		    'perPage': '1000',
		    'adminname': '',
		    'sortby': 'signupdate',
		}

		response = self.s.post('https://kiosk.pt-ka.com/api/player/list', cookies=self.s.cookies, headers=self.s.headers, data=data)
		data = response.json()

		json_str = json.dumps(data)

		# load the json to a string
		resp = json.loads(json_str)

		# extract an element in the response
		newdict = resp['result']
		for line in newdict:
			json_str2 = json.dumps(line)
			resp2 = json.loads(json_str2)
			resp2['PLAYERNAME']
			self.names.append(resp2['PLAYERNAME'])

	def getAccountNumber(self):
		numbers=[]
		for name in self.names:
			numbers.append(name[-4:])
		number = numbers[-1]
		number = int(number)
		number = number+1
		number = str(number)
		if len(number) != 4:
			missing = 4-len(number)
			if(missing == 1):
				number = '0'+number
			if(missing == 2):
				number = '00'+number
			if(missing == 3):
				number = '000'+number
		return number

manager = luckypalace()
manager.login()
manager.balance()
manager.create_player()
