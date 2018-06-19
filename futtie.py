import sys
sys.path.append('/home/maik/Downloads')

from mmoga import MMOGA
import fut
import json
import time
import random
import os
from pprint import pprint
import requests

CRED = '\r\033[91m'
CYELLOW = '\r\033[33m'
CGREEN = '\r\033[92m'
CEND = '\033[0m'


gewinn = 0
coins  = 0
os.system('clear') 
session = fut.Core('maikfischer@hotmail.de', 'Autobaum1', 'kaiee', platform='xbox')

	#item = ronaldo[0]
	#trade_id = item['tradeId']
	#trade_state = item['tradeState']
	#bid_state = item['bidState']
	#starting_bid = item['startingBid']
	#item_id = item['id']
	#timestamp = item['timestamp']  # auction start
	#rating = item['rating']
	#asset_id = item['assetId']
	#resource_id = item['resourceId']
	#item_state = item['itemState']
	#rareflag = item['rareflag']
	#formation = item['formation']
	#injury_type = item['injuryType']
	#suspension = item['suspension']
	#contract = item['contract']
	#playStyle = item['playStyle']  # used only for players	
	#discardValue = item['discardValue']
	#itemType = item['itemType']
	#owners = item['owners']
	#offers = item['offers']
	#current_bid = item['currentBid']
	#expires = item['expires']  # seconds left

def search_player(playerId, maxPrice, maxAuct, rareP, icon):
	if rareP == 'gold':
		rareP = False
	else:
		rareP = True
	ronaldo = 0
	if icon == 1:
		ronaldo = session.search(ctype = 'player', league = 2118, max_buy = maxPrice, max_price = maxAuct)
		#print(ronaldo)
		#print(maxPrice)
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
	print(str(randomNumber), end='', flush=True)
	for s in range(randomNumber, 0, -1):
		mmogaPrice()
		time.sleep(1)	
		print ("\r Loading... ".format(s)+str(s), end="")	
	print ("\r                   ".format(s)+str(s), end="")	
	
def search_reus_benzema():
	#result = search_player('50519998', '4098000')
	#print(str(result['tradeIdMin']) + ' ' + str(result['priceMin']))
	#print(str(result['tradeIdMin2']) + ' ' + str(result['priceMin2']))
	#time.sleep(5)
	result = search_player('67274017', '4098000')
	print(str(result['tradeIdMin']) + ' ' + str(result['priceMin']))
	print(str(result['tradeIdMin2']) + ' ' + str(result['priceMin2']))
	result = search_player('50496801', '4098000')
	print(str(result['tradeIdMin']) + ' ' + str(result['priceMin']))
	print(str(result['tradeIdMin2']) + ' ' + str(result['priceMin2']))
	#maskedDefId=37576

def printResult(playerName, result, rareP, maxP, printResults):
	versions = '(' + rareP + ')'
	if rareP == 'gold':
		versions = ''
	if result['length'] < 36 and result['priceMin2'] < 100000000000:
		if 'function' in str(printResults):
			printResults = 'XXXX'
		print('\r Suche: ' + playerName + versions + ' fuer ' + str(printResults) + '/' + str(maxP) + ' prices: ' + str(result['priceMin2']) + '/' + str(abrunden(abrunden(calcVerkaufsPreis(result['priceMin2'])))) + '/' + str(result['priceMin']) + ' ' + str(result['length']))	
	if result['length'] == 36:
		print('\r Suche: ' + playerName + versions + ' fuer ' + str(printResults) + '/' + str(maxP) + ' prices: ' + str(result['priceMin2']) + '/' + str(abrunden(abrunden(calcVerkaufsPreis(result['priceMin2'])))) + '/' + str(result['priceMin']) + ' ' + str(result['length']).format(s)+str(s), end='')


def verkauf(result):
	sendToList = session.sendToTradepile(item_id=result['itemId'])
	if sendToList == True:
		makeSleep()
		global gewinn 
		gewinn = gewinn + result['priceMin2']*0.95 - result['priceMin']
		verkauf = session.sell(item_id=result['itemId'], bid=preisDown(result['priceMin2']), buy_now=result['priceMin2'])
		print('\r  - - - - - - - - - > VERKAUFT für: ' + str(preisDown(result['priceMin2']))+ '/' + str(result['priceMin2']))
		#print('\r _______________________________________________________________')
		getGewinnAndCoins()
		global coins
		#print('\r  - - - - - - - - - > GEWINN: ' + str(gewinn) + '   Coins:' + str(coins))
		makeSleep()



def buyAndSell(playerName, player, rareP, icon):
	global coins	
	maxP = abrunden(random.randint(400000, 1000000))
	futpriceS = futPrice(player)
	if icon == 1:
		futpriceS = iconPrice
		playerName = "Icon"
		if coins < futpriceS:
			print(CRED + '\r not enough coins for Rare' + CEND)
			return
	if icon == 2:
		futpriceS = rarePrice
		playerName = "Rare"
		if coins < futpriceS:
			print(CRED + '\r not enough coins for Rare' + CEND)
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
				print('\r  - - - - - - - - - >  GEKAUFT für: ' + str(result['priceMin']))
				makeSleep()
				#print(session.tradepileClear())
				makeSleep()
				#print(session.relist())
			makeSleep()
			price = 0
			if icon > 0:
				price = futPriceMin(str(result['playerId']))
				difference = int(price) - int(result['priceMin2'])
				if difference < 6000:
					verkauf(result)
				else:
					print('\r AAAAAAAAAAAAAAAAAAACHHHHHHHHHHHHHHHHHHHHHHTUNGGGGGGG ' + str(difference))
			else:
				verkauf(result)

playerDict = {
#'Matthäus':        {'version': ['gold'],  	'playerId': '238436'},
#'Hagi': 	    {'version': ['gold'], 	'playerId': '239056'},
'Schweinsteiger':  {'version': ['gold'],       	'playerId': '121944'},
'Robben':	   {'version': ['gold'],       	'playerId': '9014'},
#'Hernandez1':	   {'version': ['gold'],       	'playerId': '156353'},
#'Hernandez2':	   {'version': ['gold'],       	'playerId': '238421'},
#'Hernandez3':	   {'version': ['gold'],       	'playerId': '238420'},
#'Dante':           {'version': ['gold'],       'playerId': '158625'},
'Yarmolenko':      {'version': ['gold'], 	'playerId': '194794'},
#'Donnarumma':      {'version': ['gold'], 	'playerId': '121944'},
'Coman':           {'version': ['gold'], 	'playerId': '121944'},
'Bernat':          {'version': ['gold'],       	'playerId': '205069'},
'Svensson':        {'version': ['gold'],       	'playerId': '121944'},
'Volland':         {'version': ['gold'], 	'playerId': '200610'},
'Costa':           {'version': ['gold'], 	'playerId': '190483'},
#'Promes': 	    {'version': ['gold'], 	'playerId': '208808'},
'Costa':  	   {'version': ['gold'], 	'playerId': '190483'},
'Thorgan Hazard':  {'version': ['gold'], 	'playerId': '203486'},
'Marcelo':         {'version': ['gold'], 	'playerId': '180334'},
'Joe Hart':        {'version': ['gold'], 	'playerId': '150724'},
'Aritz Elustondo': {'version': ['gold'], 	'playerId': '180334'},
'Marcelo':         {'version': ['gold'], 	'playerId': '180334'},
'Podolski':        {'version': ['gold'], 	'playerId': '150516'},
'Milinkovic-Savic':{'version': ['gold'], 	'playerId': '223848'},
'Koulibaly':       {'version': ['gold'], 	'playerId': '201024'},
'Marco Reus':	   {'version': ['gold'], 	'playerId': '188350'},
'Marc Bartra':     {'version': ['gold'], 	'playerId': '198141'},
#'Subotic':	   {'version': ['gold'], 	'playerId': '183556'},
'Sokratis':        {'version': ['gold'], 	'playerId': '172879'},
'Philipp':	   {'version': ['gold'], 	'playerId': '216497'},
'Pulisic':         {'version': ['gold'], 	'playerId': '227796'},
'Toprak':	   {'version': ['gold'],       	'playerId': '185239'},
'Piszcek':         {'version': ['gold'],       	'playerId': '173771'},
'Buerki':          {'version': ['gold'], 	'playerId': '189117'},
'Schmelzer':       {'version': ['gold'],       	'playerId': '188802'},
'Aubame':          {'version': ['gold'],  	'playerId': '188567'},
'Batsman':         {'version': ['gold'],       	'playerId': '204529'},
'Goetze':          {'version': ['gold'],  	'playerId': '192318'},
'Castro':          {'version': ['gold'],  	'playerId': '167431'},
'Hummels':         {'version': ['gold'],  	'playerId': '178603'},
'Oezil':           {'version': ['gold'],  	'playerId': '176635'},
'Boateng':         {'version': ['gold'],  	'playerId': '183907'},
'Lewandowski':     {'version': ['gold'],  	'playerId': '188545'},
'Vertonghen':      {'version': ['gold'],  	'playerId': '172871'},
'Bailly':          {'version': ['gold'],  	'playerId': '225508'},
'Jesus':           {'version': ['gold'],  	'playerId': '230666'},
'Aurier':          {'version': ['gold'],  	'playerId': '197853'},
'Alaba':           {'version': ['gold'],  	'playerId': '197445'},
'Nainggolan':      {'version': ['gold'],  	'playerId': '178518'},
'Ciciretti':       {'version': ['gold'],  	'playerId': '206160'},
'James Rodrigues': {'version': ['gold'],  	'playerId': '198710'},
'Petr Cech':       {'version': ['gold'],  	'playerId': '48940'},
'Isco':            {'version': ['gold'],  	'playerId': '197781'},
'Sneijder':        {'version': ['gold'],  	'playerId': '139869'},
'Mammana':         {'version': ['gold'],  	'playerId': '221551'},
'Fabregas':        {'version': ['gold'],  	'playerId': '162895'},
'Alderweiled':     {'version': ['gold'],  	'playerId': '184087'},
'Florentin Pgba':  {'version': ['gold'],  	'playerId': '198688'},
'Pepe':		   {'version': ['gold'],  	'playerId': '120533'},
'Gaitan':          {'version': ['gold'],  	'playerId': '184144'},
'Lacazette': 	   {'version': ['gold'],  	'playerId': '193301'},
'Kaka':		   {'version': ['gold'],  	'playerId': '138449'},
'Ibarguen': 	   {'version': ['gold'],  	'playerId': '225356'},
'Modric': 	   {'version': ['gold'],  	'playerId': '177003'},
'Rakitic': 	   {'version': ['gold'],  	'playerId': '168651'},
'Subasic': 	   {'version': ['gold'],  	'playerId': '192593'},
'Mandzukic': 	   {'version': ['gold'],  	'playerId': '181783'},
'Kovacic': 	   {'version': ['gold'],  	'playerId': '207410'},
'Vestergard': 	   {'version': ['gold'],  	'playerId': '202849'},
'Poulsen': 	   {'version': ['gold'],  	'playerId': '207791'},
'Schmeichel': 	   {'version': ['gold'],  	'playerId': '163587'},
'Delaney': 	   {'version': ['gold'],  	'playerId': '193283'},
'Messi': 	   {'version': ['gold'],  	'playerId': '158023'},
'Neymar': 	   {'version': ['gold'],  	'playerId': '190871'},
'Bale': 	   {'version': ['gold'],  	'playerId': '173731'}
}

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
	tings = session.tradepile()
	makeSleep()
	for s in tings:
		#print(s['tradeState'])
		#if s['itemState'] != 'invalid' and s['tradeState'] != 'forSale':
			#print(s['itemState'])
			#print(s['tradeState'])
		if s['tradeState'] == 'closed' and s['itemState'] == 'invalid':
			closed = closed + 1
		if s['tradeState'] == 'expired' and s['itemState'] == 'free':
			free = free + 1
	if closed > 0:
		session.tradepileClear()
		makeSleep()
		closed = 0
	if free > 0:
		session.relist()
		makeSleep()
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

def getGewinnAndCoins():
	global coins
	coins = 0
	f_in = open("coins.ini","w")
	coins = session.keepalive()
	f_in.write(str(gewinn))
	#print('\r\x1b[6;30;42m' + '_______________Coins:' + str(coins) + '_______________Gewinn:' + str(gewinn) + '_______________'+ '\x1b[0m')
	print(CGREEN + '_______________Coins:' + str(coins) + '_______________Gewinn:' + str(gewinn) + '_______________'+ CEND)
	f_in.close()

def getGewinnFromFile():
	f_out = open("coins.ini","r")
	global gewinn
	gewinn = f_out.read()
	gewinn = float(gewinn)

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
				return
			## Search mmoga player in transfermarket
			searchMmogaCard = session.search(ctype = 'player', assetId = str(searchMmoga.playerId), min_buy = 10000, min_price = str(searchMmoga.startBid))
			#print(str(searchMmoga.playerId))
			#print(str(searchMmoga.startBid))
			## Get Item-Id
			item_id = ''
			for details in searchMmogaCard:
				trade_id = details['tradeId']
				if trade_id == searchMmoga.playerId:
					item_id = p['id']

			## Bid on mmoga player
			print(str(searchMmoga.tradeId))
			kaufMmogaCard = session.bid(trade_id=str(searchMmoga.tradeId), bid=10000, fast=True)
			
			# Selling check
			if kaufMmogaCard == True:
				#print('ItemID'+str(item_id))
				if item_id != '':
					session.sendToClub(searchMmoga.playerId, item_id)
					print('\r Sent to Club')
				searchMmoga.cofirmMMOGA()
				gewinn = gewinn - 7000
				print(CYELLOW +' MMOGA-sell perfect'+ CEND)
			else:
				print(kaufMmogaCard)
			del searchMmoga
getGewinnFromFile()
iconPrice = 155000
rarePrice = 10000
for a in range(0,20):
	for s in range(0,10):
		getGewinnAndCoins()
		deleteTradepile()
		searchLoop()
	time.sleep(15)	
if __name__ == '__main__':
    main()
