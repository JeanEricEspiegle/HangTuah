import requests
import json

class Manager():
	def login(self):
		login_url = 'https://mgoapi-aws.szjfqczl.com/megagw/api/gw.mega.agent.login'
		login_parameters = {"id":1659256712926,"params":{"opsId":"ld001D9727A922768A03FB37B2553fc6","host":"k.mega688.com","loginId":"MEGA88-MIKE","saltedPassword":"14/xalN9XKgeqCESrq62S5umXUw=","sn":"ld00","salt":1659256712925},"jsonrpc":"2.0","method":"gw.mega.agent.login"}
		response = requests.post(login_url, json=login_parameters)

		data = response.json()

		for key, value in data.items():
		         if "result" == key:
		            rdata = value

		for key, value in rdata.items():
		         if 'sessionId' == key:
		            sessionID = value
		return sessionID

	def topup(self,amount, targetid):
		sessionID = self.login()
		topup_url = 'https://mgoapi-aws.szjfqczl.com/megagw/api/mega.user.balance.transfer'
		topup_parameters = {"id":1659254731079,"params":{"opsId":sessionID,"sourceUid":"496445353","targetUid":targetid,"amount":amount,"userType":"1","agentId":"496445353"},"jsonrpc":"2.0","method":"mega.user.balance.transfer"}
		response = requests.post(topup_url, json=topup_parameters)

		data = response.json()
		return response.status_code

	def search(self,ID):
		sessionID = self.login()
		search_url='https://mgoapi-aws.szjfqczl.com/megagw/api/gw.mega.account.search'
		search_parameters= {"id":1659414965909,"params":{"opsId":sessionID,"pageIndex":1,"pageSize":10,"userLoginId":ID},"jsonrpc":"2.0","method":"gw.mega.account.search"}
		
		response = requests.post(search_url, json=search_parameters)

		data = response.json()
		for key, value in data.items():
		         if "result" == key:
		            rdata = value

		for key, value in rdata.items():
		         if 'user' == key:
		            udata= value

		for key, value in udata.items():
		         if 'amount' == key:
		            amountdata = value

		for key, value in udata.items():
		         if 'userId' == key:
		            targetid = value

		return amountdata, udata, targetid

	def CreateNewMember(self):
		sessionID = self.login()
		areacode = None
		areacode_url='https://mgoapi-aws.szjfqczl.com/megagw/api/gw.mega.user.area.code.get'
		areacode_parameters={"id":1659417026477,"params":{"opsId":sessionID},"jsonrpc":"2.0","method":"gw.mega.user.area.code.get"}
		response = requests.post(areacode_url, json=areacode_parameters)

		data = response.json()

		for key, value in data.items():
		         if "result" == key:
		            areacode = value

		generate_url='https://mgoapi-aws.szjfqczl.com/megagw/api/gw.mega.user.loginId.generate'
		generate_parameters= {"id":1659415443575,"params":{"opsId":sessionID,"areaCode":areacode},"jsonrpc":"2.0","method":"gw.mega.user.loginId.generate"}
		
		response2 = requests.post(generate_url, json=generate_parameters)

		data2 = response2.json()

		for key, value in data2.items():
		         if "result" == key:
		            userID = value

		create_url='https://mgoapi-aws.szjfqczl.com/megagw/api/mega.user.add'
		create_parameters= {"id":1659415554019,"params":{"opsId":sessionID,"password":"GiwYHQ9iq8n5JrpbUxABt7TRzkY=","amount":"0","nickname":"","tel":"","memo":"","textPwd":"Aaa123","agentLoginId":"MEGA88-MIKE","agentId":"496445353","loginId":userID},"jsonrpc":"2.0","method":"mega.user.add"}
		response3 = requests.post(create_url, json=create_parameters)

		data3 = response3.json()

		for key, value in data3.items():
		         if "result" == key:
		            resultdata = value

		for key, value in resultdata.items():
		         if "success" == key:
		            adddata = value

		return userID,adddata