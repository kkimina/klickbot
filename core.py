import sys
sys.path.append('/home/maik/Downloads')

import fut
import json
import time
import random
import os
from pprint import pprint
import requests
import tkinter
from tkinter import *

CRED = '\r\033[91m'
CYELLOW = '\r\033[33m'
CGREEN = '\r\033[92m'
CEND = '\033[0m'

 
class CORE:
	gewinn   		= 0
	coins    		= 0
	passwort        = ''
	account         = ''
	platform        = ''
	sicherheitskey  = ''
	session         = ''
	w		= ''
	gui		= ''
	
	def initGui(self):
		self.gui = tkinter.Tk()
	
	def showGui(self):
		self.gui.update_idletasks()

	def refreshGewinn(self):
		self.w = Label(self.gui, text='Gewinn: ' + str(self.gewinn))
		self.w.pack()

	
	def refreshCoins(self):
		self.w = Label(self.gui, text='Coins: ' + str(self.coins))
		self.w.pack()

	def init(self, acount, passwort, platform, key):
		self.account 	     = account
		self.passwort        = passwort
		self.platform        = platform
		self.sicherheitskey  = key

	def connect(self):
		self.session = fut.Core(self.account, self.passwort, self.sicherheitskey, platform=self.platform)

	def search_player(playerId, maxPrice, maxAuct, rareP, icon):
		if rareP == 'gold':
			rareP = False
		else:
			rareP = True
		ronaldo = 0
		if icon == 1:
			ronaldo = session.search(ctype = 'player', league = 2118, max_buy = maxPrice, max_price = maxAuct)
		if icon == 0:
			ronaldo = session.search(ctype = 'player', assetId = playerId, max_buy = maxPrice, max_price = maxAuct, rare = rareP)
		if icon == 2:
			ronaldo = session.search(ctype = 'player', max_buy = maxPrice, max_price = maxAuct, rare = True)
		minimum = 100000000000
		minimum2= 100000000000
		trade_id_min = ""
		item_id = ""
		trade_id_min2= ""
		player_id = ""
		for p in ronaldo:
			trade_id = p['tradeId']
			buy_now_price = p['buyNowPrice']
			if buy_now_price <= minimum:
				if minimum != 100000000000:
					minimum2 = minimum
					trade_id_min2 = trade_id_min	
				minimum = buy_now_price
				trade_id_min = trade_id
				item_id = p['id']
				player_id = p['assetId']
			#print(p['buyNowPrice'])
			#print(p['rareflag'])
		return {'length': len(ronaldo), 'itemId': item_id, 'tradeIdMin': trade_id_min, 'priceMin': minimum, 'tradeIdMin2': trade_id_min2, 'priceMin2': minimum2, 'playerId': player_id}
	
	
	
	def abrunden(zahl):
		zahl = int(zahl)
		if zahl < 1000:
			return int(round(zahl/50)*50)
		elif zahl >= 1000 & zahl < 10000:
			return int(round(zahl/100)*100)
		elif zahl >= 10000 & zahl < 50000:
			return int(round(zahl/250)*250)
		elif zahl >= 50000 & zahl < 100000:
			return int(round(zahl/500)*500)
		else:
			return 0
		
	
	def preisDown(zahl):
		zahl = int(zahl)
		if zahl <= 1000:
			return zahl - 50
		elif zahl > 1000 and zahl <= 10000:
			return zahl - 100
		elif zahl > 10000 and zahl <= 50000:
			return zahl - 250
		elif zahl > 50000 and zahl <= 100000:
			return zahl - 500
		elif zahl > 100000 and zahl <= 500000:
			return zahl - 1000
		else:
			return 0
	
	def preisUp(zahl):
		zahl = int(zahl)
		if zahl < 1000:
			return zahl + 50
		elif zahl >= 1000 and zahl < 10000:
			return zahl + 100
		elif zahl >= 10000 and zahl < 50000:
			return zahl + 250
		elif zahl >= 50000 and zahl < 100000:
			return zahl + 500
		elif zahl >= 100000 and zahl < 500000:
			return zahl + 1000
		else:
			return 0
	
	
	def calcVerkaufsPreis(preis):
		if preis >= 100 & preis < 500:
			return (preis * 0.95) - 100
		elif preis >= 500 & preis < 2000:
			return (preis * 0.95) - 200
		elif preis >= 2000 & preis < 5000:
			return (preis * 0.95) - 400
		elif preis >= 5000 & preis < 10000:
			return (preis * 0.95) - 600
		elif preis >= 10000 & preis < 20000:
				return (preis * 0.95) - 2000
		elif preis >= 20000 & preis < 30000:
			return (preis * 0.95) - 2000
		elif preis >= 30000 & preis < 40000:
			return (preis * 0.95) - 2000
		elif preis >= 40000 & preis < 50000:
			return (preis * 0.95) - 3000
		elif preis >= 50000 & preis < 150000:
			return (preis * 0.95) - 3000
		elif preis >= 150000 & preis < 200000:
			return (preis * 0.95) - 5000
		elif preis >= 200000 & preis < 300000:
			return (preis * 0.95) - 5000
		elif preis >= 300000 & preis < 400000:
			return (preis * 0.95) - 5000
		else:
			return (preis * 0.85)
	
	
	def makeSleep():
		randomNumber = random.randint(5,14)
		for s in range(randomNumber, -1, -1):
			mmogaPrice()
			time.sleep(1)	
			print ("\r Loading... ".format(s)+str(s) + "                                                        ", end="")
	
	def printResult(playerName, result, rareP, maxP, printResults):
		versions = '(' + rareP + ')'
		if rareP == 'gold':
			versions = ''
		if result['length'] < 36 and result['priceMin2'] < 100000000000:
			if 'function' in str(printResults):
				printResults = 'XXXX'
			print('\r Suche: ' + playerName + versions + ' fuer ' + str(printResults) + '/' + str(maxP) + ' prices: ' + str(result['priceMin2']) + '/' + str(abrunden(abrunden(calcVerkaufsPreis(result['priceMin2'])))) + '/' + str(result['priceMin']) + ' ' + str(result['length']) + '        ')	
		if result['length'] == 36:
			print('\r Suche: ' + playerName + versions + ' fuer ' + str(printResults) + '/' + str(maxP) + ' prices: ' + str(result['priceMin2']) + '/' + str(abrunden(abrunden(calcVerkaufsPreis(result['priceMin2'])))) + '/' + str(result['priceMin']) + ' ' + str(result['length']).format(s)+str(s), end='')
	
	
	def verkauf(result):
		sendToList = session.sendToTradepile(item_id=result['itemId'])
		if sendToList == True:
			makeSleep()
			global gewinn 
			gewinn = gewinn + result['priceMin2']*0.95 - result['priceMin']
			verkauf = session.sell(item_id=result['itemId'], bid=preisDown(result['priceMin2']), buy_now=result['priceMin2'])
			print('\r  - - - - - - - - - > VERKAUFT für: ' + str(preisDown(result['priceMin2']))+ '/' + str(result['priceMin2'])+ '             ')
			getGewinnAndCoins()
			makeSleep()
	
	
	
	def buyAndSell(playerName, player, rareP, icon):
		global coins	
		maxP = abrunden(random.randint(400000, 1000000))
		futpriceS = futPrice(player)
		if icon == 1:
			futpriceS = iconPrice
			playerName = "Icon"
			if coins < futpriceS:
				print(CRED + '\r not enough coins for Icon                                        ' + CEND)
				return
		if icon == 2:
			futpriceS = rarePrice
			playerName = "Rare"
			if coins < futpriceS:
				print(CRED + '\r not enough coins for Rare                                        ' + CEND)
				return
		result = search_player(player, futpriceS, maxP, rareP, icon)
		printResult(playerName, result, rareP, maxP, futpriceS)
		while result['length'] == 36:
			makeSleep()
			if result['priceMin'] == result['priceMin2']:
				result['priceMin'] = preisDown(result['priceMin'])
			result = search_player(player, result['priceMin'], maxP, rareP, icon)
		if abrunden(abrunden(calcVerkaufsPreis(result['priceMin2']))) >= result['priceMin']:
			if result['priceMin2'] < 100000000000 and coins > result['priceMin']:
				kauf = session.bid(trade_id=result['tradeIdMin'], bid=result['priceMin'], fast=True)
				if kauf == True:
					print('\r  - - - - - - - - - >  GEKAUFT für: ' + str(result['priceMin'])+ '                                   ')
					makeSleep()
					session.tradepileClear()
					makeSleep()
					session.relist()
				makeSleep()
				price = 0
				if icon > 0:
					price = futPriceMin(str(result['playerId']))
					difference = int(price) - int(result['priceMin2'])
					verkauf(result)
				else:
					verkauf(result)
	
	
	def futPrice(id):
		r = requests.get('http://www.futbin.com/18/playerPrices?player='+id+'&all_versions=&_=1')
		output = r.text
		#print(output)
		split = output.split(':{"')
		splitXbox = split[3].split('","')
		for s in splitXbox:
			splitS = s.split('":"')
			value = splitS[1].replace(',', '')
			value = value.replace('"}"ps"', '')
			if splitS[0] == 'LCPrice2':
				#print(value)
				return value
	def futPriceMin(id):
		r = requests.get('http://www.futbin.com/18/playerPrices?player='+id+'&all_versions=&_=1')
		output = r.text
		#print(output)
		split = output.split(':{"')
		splitXbox = split[3].split('","')
		for s in splitXbox:
			splitS = s.split('":"')
			value = splitS[1].replace(',', '')
			value = value.replace('"}"ps"', '')
			if splitS[0] == 'LCPrice':
				#print(value)
				return value
	
	def deleteTradepile():
		closed = 0
		free = 0
		tings = self.session.tradepile()
		self.makeSleep()
		for s in tings:
			if s['tradeState'] == 'closed' and s['itemState'] == 'invalid':
				closed = closed + 1
			if s['tradeState'] == 'expired' and s['itemState'] == 'free':
				free = free + 1
		if closed > 0:
			self.session.tradepileClear()
			self.makeSleep()
			closed = 0
		if free > 0:
			self.session.relist()
			self.makeSleep()
			free = 0
	
	def searchLoop():
		for r in range(5):
			elements = 0
			playerNumber = random.randint(0,len(playerDict.keys()))
			for key in playerDict.keys():
				elements = elements + 1
				if elements == playerNumber:
					for version in playerDict[key]['version']:
						buyAndSell(key, playerDict[key]['playerId'], version, 0)
						makeSleep()
						buyAndSell(key, playerDict[key]['playerId'], version, 1)
						makeSleep()
						buyAndSell(key, playerDict[key]['playerId'], version, 2)
						makeSleep()
	
	def getGewinnAndCoins(self):
		self.coins = 0
		f_in = open("coins.ini","w")
		self.coins = self.session.keepalive()
		f_in.write(str(self.gewinn))
		print(CGREEN + '_______________Coins:' + str(self.coins) + '_______________Gewinn:' + str(self.gewinn) + '_______________        '+ CEND)
		f_in.close()
	
	def getGewinnFromFile(self):
		f_out = open("coins.ini","r")
		self.gewinn = f_out.read()
		self.gewinn = float(self.gewinn)
	
	def mmogaPrice():
		global gewinn
		if gewinn >7000:
			searchMmoga = MMOGA()
			searchMmoga.makeFirstStep()
			searchMmoga.writeMMOGAcookies()
			searchMmoga.getPriceAndAmount()
			if searchMmoga.amount > 1:
				searchMmoga.makeNextSteps()
				test = searchMmoga.getPlayerDetails()
				if test == 0:
					print(CRED + 'player-Details = 0' + CEND)
					return
				## Search mmoga player in transfermarket
				searchMmogaCard = session.search(ctype = 'player', assetId = str(searchMmoga.playerId), min_buy = 10000, min_price = str(searchMmoga.startBid))
	
				## Get Item-Id
				item_id = ''
				for details in searchMmogaCard:
					#print('tradeId: ' + str(details['tradeId']))
					#print('details: ' + str(details))
					trade_id = details['tradeId']
					if str(trade_id) == str(searchMmoga.tradeId):
						item_id = details['id']
						print(CYELLOW + 'MATCHED                                                 ' + CEND)
	
				## Bid on mmoga player
				kaufMmogaCard = session.bid(trade_id=str(searchMmoga.tradeId), bid=10000, fast=True)
				
				# Selling check
				if kaufMmogaCard == True:
					if item_id != '':
						session.sendToClub(item_id)
						print(CYELLOW + 'Sent to Club              ' + CEND)
					searchMmoga.cofirmMMOGA()
					gewinn = gewinn - 7000
					print(CYELLOW +' MMOGA-sell perfect                                               '+ CEND)
				else:
					print('KaufMMogaCard: ' + kaufMmogaCard)
				del searchMmoga
