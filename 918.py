import requests
import json
import time
import logging
from bs4 import BeautifulSoup
import objectpath


class kiss():
	s = requests.Session()
	headers = {
		    'authority': 'kk2.918kiss.com',
		    'accept': 'application/json, text/javascript, */*',
		    'accept-language': 'en-US,en;q=0.9',
		    # Requests sorts cookies= alphabetically
		    # 'cookie': '_ga=GA1.2.1760724254.1659503561; _ym_d=1659503561; _ym_uid=1659503561252526900; ASP.NET_SessionId=4qdhvi33k1grqvaepsmayseq',
		    'origin': 'https://kk2.918kiss.com',
		    'referer': 'https://kk2.918kiss.com/Login.aspx?rt=0.34573587880889756',
		    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
		    'sec-ch-ua-mobile': '?0',
		    'sec-ch-ua-platform': '"Windows"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'same-origin',
		    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
		    'x-requested-with': 'XMLHttpRequest',
		}
	def login(self):
		uName = 'KISS68-243'
		pw = 'Rose8888'
		pw2 = '789789'

		cookies = {
		    '_ga': 'GA1.2.1760724254.1659503561',
		    '_ym_d': '1659503561',
		    '_ym_uid': '1659503561252526900',
		    'ASP.NET_SessionId': '4qdhvi33k1grqvaepsmayseq',
		}
		
		data = {
		    'action': 'login',
		    'userName': uName,
		    'passWd': pw,
		    'country': 'N/A',
		    'city': 'N/A',
		}
		response = self.s.post('https://kk2.918kiss.com/login/WebUserLogin.ashx', cookies=cookies, headers=self.headers, data=data)
		cookies = response.cookies

		data = {
		    'action': 'CheckSecondPwd',
		    'userName': uName,
		    'secondPassWd': pw2,
		    'CurDateTime': '3308471',
		}

		response = self.s.post('https://kk2.918kiss.com/login/WebUserLogin.ashx', cookies=cookies, headers=self.headers, data=data)
		cookies = response.cookies
		data = {
		    'action': 'CheckLogin',
		    'CurDateTime': '4936386',
		}

		response = self.s.post('https://kk2.918kiss.com/ashx/login/CheckLogin.ashx', cookies=cookies, headers=self.headers, data=data)
		#print(response.json())


	def search(self,ID):
		payload = 'https://kk2.918kiss.com/ashx/account/account.ashx?action=getSearchUserInfo&userName='+ID+'&CurDateTime=2154836'
		searchR = self.s.post(payload)
		data = searchR.json()
		print(data)

	def getPlayersList(self):
		cookies = {
		    '_ga': 'GA1.2.1760724254.1659503561',
		    '_ym_d': '1659503561',
		    '_ym_uid': '1659503561252526900',
		    'ASP.NET_SessionId': 'x3fwlh5q2xlfcfkwumjk4pty',
		    '_dtmadcsw': '6CC861A6DD4014CA3C38049F857DE08DB5C50A184607BFACBD7541FF5C0154AE73F0689EDC9C0BF75863263C05AF7EF8FF573AE24BF2F4093CFD115B3BD2A9B27F1533999DDEF490560AA3F615DBE62C4B30A9DB08ECB74248B3C37D50DDA4C9C8CDAFA778A1A19FA26B0A7D5025762348BC38A370CA1FC6215C7B39E962057E08A3FA2C63C7C26B1A7BE2203FD92B89',
		    'MCookiesw': 'F2E24AFC155923A78D13069DD2BDDCD65A0B17113B34660F13FFCA5A7E00ADE00BA3BF33E064773B44A929EBFC83667B7B240C8D2A427DC2A78E61A0EA297C2E16F4F43F9ECBF1B022624C629E55B51F967BFD1A768DCED7FF0429BECD5AA48A6D83CD46D7B9412D0BE1313E2E80CDD3EA40CB1B49D83628D3CC916A67387CDE55FE8B05AD95DF107EB89005AD2B5A73BFB9A7AEC93AA854969CD7E64C0DFD2026FA1718BEE83173E8451BCB569820E7353B94E7456CE20C3297AEAA3A87CCBBEE942AD364CDEA9D0316BC0702AB1D8C81D49553B21D3C3BE6C12DAF89584C8BF4AA51E719E86A041A5A78E4C347C8C71DC9AFFF20CD6F7507E7E3C1E62A89488E91935C875B33B2843E997861931E1B2C198158C1E9E81ACC2A05A967D870803EAF4B62C7733432FBAE13B0CA47C463884466F26A56844D325F27324E905D189EFFF09786AA96C67593F14D62B4CDB35B8183F5C1AA9AD5278D57D9AD459D9AC6DF8F0B32F1312A3891F5CC28752546A75A829CF370713F9F56740EFF7BB20E41800C9ED75DA2DC8B9296A939FC7F7FA9FFEC81276103C99CF48B1AE0E2E53ECA0D31024C4197B08821464AB117DF4E8081868317DA6773DC88D575722EA8726A9EB975EBB64B3B61E620152B0F0C48E6FF4EFC32D95D3C9202CB77B6B9557FA7BDC4DCA654ADF0A56CC2A721B8FF930DB125C09B417E99744B8939E2D0FF435E684385D787A1C8A8554C82E0C0F716336883A375085634A3EA9A98F859F8B3E4DB17AE83F93C8E34220ACAE4E5AC6D8FDE29543ABEB23A58D2FAB80DC695746259F6A3A36F87CD99AF43412C423EA773DD639B75B116034A3C5D46CAEF40493D32F8B7F29DFA7F8D97573D7D4E2D07ADB3623C07F28874CBB6D78D59F197AD19E4C35C8A54A1C252932BE189D584C71B1C7E693BAA0CA8D8604DF61A8234FB0689DD6BBA1AA2C27FA0CA819D87E3F665E5653A7F5EBC9684419173E76A4BC9D7DE8D1C6D11AB41B4EC190DA3F556F0A1A13969FE2308FCA5CF2DC4FF92D43B4209A1F8FB7FC4FE77E56799214628AFC96EDE509C85EDD3B337703F33D0EAD51F069A3F267AA768EEE658DDA2D155266A8427EF240D75DAC52D8F4CA6E4D22A4A106D5C26E2200DC5C9E841EB1A8C34A7089A405A92C643EF30ECCE3B1A1DCCC1553C2534EBB358945D84B2C42B320ED4BBD0BD8F79DC35E11B893D6461C94DA2D5E37E8278DB96166FB256F6BEB28060210CB58FF4AC21EFCC47D6B146CD67F62A4D38F710BE6693308B005A20AFA7748C86EBDBEC23A1CA37329B4BBBCC7CDD6F2EE4E1C98AB43F926BF28FC5A49B22B7A5FCA3FF94C3D50684CA12DD730C961D46200179FBBAFEFEAE02A5A4153C2AA1AD7BE0C33E1B4935F9C9746485CDED84FAEF47067C9EFE954BF22679A325881A12C8069D499F3E8774B48B9AA2FEC409EC2654907F766391FC1DAD940313DE41C59E036DBA7210FC6AF0751659C023B541A7662B516B1CDA858E7A6278B5AE2F9D6CFDA7F1462EEE31E9A4A2F72EFD1079FC9D4C1CFCAEB81CCE2C32E3B715974DF37DA9278C9C60DE036E85E8C8CC1D7D4FCF9ED487E3D14599F18C8557896550623589AE2482A8B3042E8960B12D861C960930EEC19168B421BD27B0CCE485D106A5A4DF1E727532CC08676D1663961CBA3CD19B08C76431DAB215FC7E',
		}
		for x in range(1,12):
			data = {
				'action': 'playerList',
				'userName': 'kiss68-243',
				'pageIndex': str(x),
				'pageSize': '20',
				'isReload': '0',
				'CurDateTime': '2022-08-20',
			}
			response = self.s.post('https://kk2.918kiss.com/ashx/getData/AccountList.ashx', headers=self.headers, data=data)
			data = response.json()
			tree_obj = objectpath.Tree(data)
			accounts = tuple(tree_obj.execute('$..Account'))
			for i in range(0,len(accounts)):
				payload = 'https://kk2.918kiss.com/ashx/account/AccountInfo.ashx?action=GetAreaMoneyInfo&userName='+accounts[i]
				response = self.s.post(payload)
				data2 = response.json()
				money_tree = objectpath.Tree(data2)
				money  = tuple(money_tree.execute('$..money'))
				print(i,money[0])
				if(int(money[0]) > 0):
					data = {
					    'action': 'setServerScore',
					    'scoreNum': '-2',
					    'MaxNum': '772.34',
					    'userName': accounts[i],
					    'CurDateTime': '291238',
					}
					response = self.s.post('https://kk2.918kiss.com/ashx/account/setScore.ashx', data=data)
					data = response.json()
					print(data)

	def disable(self,playerId):
		data = {
		    'action': 'disable',
		    'user': playerID,
		    'rand': '7870542',
		}

		response = requests.post('https://kk2.918kiss.com/ashx/account/account.ashx', data=data)


kiss = kiss()
kiss.login()
