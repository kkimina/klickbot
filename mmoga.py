import requests
import time
import atexit
import os

CRED = '\r\033[91m'
CYELLOW = '\r\033[33m'
CEND = '\033[0m'

class MMOGA:
	MMOGAsid	= ''
	mmddd		= ''
	xboxPrice	= 0
	amount		= 0
	playerId	= 0
	startBid	= 0
	tradeId		= 0
	mid		= 0
	key		= 0
	expires		= 0
	futWebExpires   = 0


	url   		= 'https://www.mmoga.de/FIFA-Coins/FUT-Coins-Verkaufen/'

	mmogaSession	= requests.Session()

	step2 = 'step=2&platform=Xbox_One'
	step3 = 'step=3&coins=10'
	step4 = 'step=4&payment=skrill&paypal_email=&paypal_email_confirm=&skrill_email=maikfischer%40hotmail.de&skrill_email_confirm=maikfischer%40hotmail.de'
	step5 = ''

	step1Answer = ''
	step2Answer = ''
	step3Answer = ''
	step4Answer = ''
	step5Answer = ''

	postheaders 	= {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    	'Accept-Encoding': 'gzip,deflate,sdch, br',
	'Accept-Language': 'en-US,en;q=0.8',
	'origin': 'https://www.mmoga.de',
	'referer': 'https://www.mmoga.de/FIFA-Coins/FUT-Coins-Verkaufen/',
	'Host': 'www.mmoga.de',
	'Connection': 'keep-alive',
	'Content-Type': 'application/x-www-form-urlencoded'
	}

	def beepingsound():
		beep = lambda x: os.system("echo -n '\a';sleep 0.2;" * x)
		beep(3)

	def getPriceAndAmount(self):
		if self.step1Answer == '':
			print('\r'+' should not happen -> getPriceAndAmount')
			return
		split = self.step1Answer.text.split('<p class="futSellT">Fifa 18 Coins - Xbox One</p>')
		splitXbox = split[1].split('<p>')		
		splitEuro = splitXbox[1].split('&nbsp;&euro')
		splitEuro = splitEuro[0].split('100k: ')
		wert = splitEuro[1]
		wert2 = wert.replace(',', ".")
		self.xboxPrice = float(wert2)

		splitBedarf = splitXbox[1].split('<br>Bedarf: ')
		splitBedarf = splitBedarf[1].split('k</p>')
		self.amount = int(splitBedarf[0])
		#print( str(self.xboxPrice) + " " + str(self.amount))

	def makeFirstStep(self):
		answer = requests.get(self.url)
		if '<input type="hidden" name="step" id="step" value="2">' in answer.text:
			self.step1Answer = answer
		else:
			print('\r'+'something wrong')


	def writeMMOGAcookies(self):
		if self.step1Answer == '':
			print('\r'+'no coins')
		#	return
		self.MMOGAsid		= self.step1Answer.cookies['MMOGAsid']
		self.mmddd		= self.step1Answer.cookies['mmddd']
		self.mmogaSession.cookies.set('MMOGAsid', self.MMOGAsid)
		self.mmogaSession.cookies.set('mmddd'   , self.mmddd)
		self.mmogaSession.cookies.set('cookie_test', 'please_accept_for_session')

	def makeNextSteps(self):
		if self.amount == 0:
			print('\r'+ str(self.xboxPrice) + " " + str(self.amount))
		#		return
		answer2 = self.mmogaSession.post(self.url, data=self.step2, headers=self.postheaders)
		if '<input type="hidden" name="step" id="step" value="3">' in answer2.text:
			self.step2Answer = answer2
		else:
			print('\r'+'something wrong')
		answer3 = self.mmogaSession.post(self.url, data=self.step3, headers=self.postheaders)
		if '<input type="hidden" name="step" id="step" value="4">' in answer3.text:
			self.step3Answer = answer3
		else:
			print('\r'+'something wrong')
		self.step4Answer = self.mmogaSession.post(self.url, data=self.step4, headers=self.postheaders)
		#print(self.step4Answer.text)

	def cofirmMMOGA(self):
		if self.step5 == '':
			print('\r'+'no confirmation possible')
			return
		self.step5Answer = self.mmogaSession.post(self.url, data=self.step5, headers=self.postheaders)
		#print(self.step5Answer.text)
		print(CYELLOW + 'MMOGA-Confirmation complete   ' + CEND)

	def getPlayerDetails(self):
		if self.step4Answer == '':
			print(CRED + 'MMOGA: no coins                  ' + CEND)
			return
		if 'Sie haben noch eine andere offene Auktion' in self.step4Answer.text:
			print(CRED + 'MMOGA: auction ongoing           ' + CEND)
			return 0
		if 'Leider' in self.step4Answer.text:
			print(CRED + 'MMOGA: to late                   ' + CEND)
			return 0
		if '<div class="futSellPayL">Player ID:</div>' in self.step4Answer.text:
			print()
		else:
			print(self.step4Answer.text)
			print(CRED + 'MMOGA: keine PlayerID            ' + CEND)
			return 0
		## get player-id
		print(CYELLOW +' - - - - - - MMOGA VERKAUF - - - - - - '+ CEND)
		#print(self.step4Answer.text)
		mmogaPlayerId = self.step4Answer.text.split('<div class="futSellPayL">Player ID:</div>')
		mmogaPlayerId = mmogaPlayerId[1].split('<div class="futSellPayR">')
		mmogaPlayerId = mmogaPlayerId[1].split('</div>')
		mmogaPlayerId = mmogaPlayerId[0]
		self.playerId = mmogaPlayerId

		## get starting-bid
		mmogaStartBid = self.step4Answer.text.split('<div class="futSellPayL">Startpreis:</div>')
		mmogaStartBid = mmogaStartBid[1].split('<div class="futSellPayR">')
		mmogaStartBid = mmogaStartBid[1].split('</div>')
		mmogaStartBid = mmogaStartBid[0]
		self.startBid = mmogaStartBid

		## get trade-id
		mmogaTradeId = self.step4Answer.text.split('<div class="futSellPayL">Trade ID:</div>')
		mmogaTradeId = mmogaTradeId[1].split('<div class="futSellPayR">')
		mmogaTradeId = mmogaTradeId[1].split('</div>')
		mmogaTradeId = mmogaTradeId[0]
		self.tradeId = mmogaTradeId

		## get mmogaId
		mmogaId  = self.step4Answer.text.split('<input type="hidden" name="id" id="id" value="')
		mmogaId  = mmogaId[1].split('">')
		mmogaId	 = mmogaId[0]
		self.mid = mmogaId	

		## get mmogaKey
		mmogaKey = self.step4Answer.text.split('<input type="hidden" name="key" id="key" value="')
		mmogaKey = mmogaKey[1].split('">')
		mmogaKey = mmogaKey[0]
		self.key = mmogaKey		

		## get mmogaExpires
		mmogaExpires = self.step4Answer.text.split('<input type="hidden" name="expires" id="expires" value="')
		mmogaExpires = mmogaExpires[1].split('">')
		mmogaExpires = mmogaExpires[0]
		self.expires = mmogaExpires

		## get mmogaFutWebExpires
		mmogaFutWebExpires = self.step4Answer.text.split('<input type="hidden" name="futwebExpires" id="futwebExpires" value="')
		mmogaFutWebExpires = mmogaFutWebExpires[1].split('">')
		mmogaFutWebExpires = mmogaFutWebExpires[0]
		self.futWebExpires = mmogaFutWebExpires
		
		## create comfirm content
		self.step5 = 'step=5&id='+str(self.mid)+'&key='+str(self.key)+'&expires='+str(self.expires)+'&futwebExpires='+str(self.futWebExpires)
		#print(self.step5)

