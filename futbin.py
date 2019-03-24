import json
import requests

IF = 'IF'
TOTGS = 'TOTGS'
CL = 'CL'
NORMAL = 'Normal'
SWAP = 'Swap Deal Reward SBC'
POTM = 'Bundes POTM'
SIF = 'SIF'
UCL = 'UCL LIVE'
HALLOWEEN = 'Halloween'
OTW = 'OTW'


class FUTBIN:
    def __init__(self):
        self.rare_list = {}
        self.normal_list = {}
        self.min_rare             = 0
        self.normal               = 0
        self.einkaufspreis_normal = 0
        self.einkaufspreis_rare   = 0
        self.verkauf              = 0
        self.einkauf              = 0
        self.time_normal          = -1
        self.time_rare            = -1

    def fillPrices(self, name):
        try:
            output = requests.get('https://www.futbin.com/search?year=19&extra=1&term=' + str(name)).text
            jsonOutput = json.loads(output)

            for s in jsonOutput:
                output2 = requests.get('https://www.futbin.com/19/player/' + str(s['id'])).text
                split = output2.split('data-player-resource="')
                allVersions = split[1].split('data-id')
                allVersions = allVersions[0].split('"')
                output3 = requests.get('https://www.futbin.com/19/playerPrices?player=' + str(allVersions[0])).text
                jsonPrices = json.loads(output3)
                for versions in jsonPrices:
                    sum = jsonPrices[versions]['prices']['xbox']['LCPrice2'].replace(',', '')
                    time = jsonPrices[versions]['prices']['xbox']['updated']
                    time = time.replace(' mins ago', '')
                    time = time.replace(' min ago', '')
                    time = time.replace(' secs ago', '')
                    time = time.replace(' sec ago', '')
                    if 'ago' not in time and 'Never' not in time:
                        self.rare_list[s['version'] + '_time'] = int(time)
                        self.rare_list[s['version']] = int(sum)
                    else:
                        print(time + ' error')
        except:
            print('error by ' + name)
            self.fillPrices(name)

    def getMinPrices(self):
        for h in self.rare_list.keys():
            if '_time' not in h:
                if h == 'Normal' or h == 'Winter Refresh':
                    if self.normal is 0:
                        self.normal = self.rare_list[h]
                    else:
                        if self.rare_list[h] < self.normal:
                            self.normal = self.rare_list[h]
                    self.time_normal =self.rare_list[h + '_time']

                else:
                    if self.min_rare == 0 and self.rare_list[h] != 0:
                        self.min_rare = self.rare_list[h]
                    else:
                        if self.rare_list[h] < self.min_rare:
                            self.min_rare = self.rare_list[h]
                    self.time_rare = self.rare_list[h + '_time']

        self.einkaufspreis_rare   = self.abrunden(self.preisDown(self.calcVerkaufsPreis(self.min_rare)))
        self.einkaufspreis_normal = self.abrunden(self.preisDown(self.calcVerkaufsPreis(self.normal)))

    def preisDown(self, zahl):
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

    def abrunden(self, zahl):
        zahl = int(zahl)
        if zahl < 1000:
            return int(round(zahl / 50) * 50)
        elif zahl >= 1000 & zahl < 10000:
            return int(round(zahl / 100) * 100)
        elif zahl >= 10000 & zahl < 50000:
            return int(round(zahl / 250) * 250)
        elif zahl >= 50000 & zahl < 100000:
            return int(round(zahl / 500) * 500)
        else:
            return 0

    def preisUp(self, zahl):
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

    def calcVerkaufsPreis(self, preis):
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

    def getEinkaufVerkaufPrices(self, quality):
        if quality == 'gold':
            self.verkauf = self.normal
            self.einkauf = self.einkaufspreis_normal
            self.time    = self.time_normal
        else:
            self.verkauf = self.min_rare
            self.einkauf = self.einkaufspreis_rare
            self.time    = self.time_rare

    def calculatePrices(self, player, quality):
        self.fillPrices(player)
        self.getMinPrices()
        self.getEinkaufVerkaufPrices(quality)


#price = FUTBIN()
#price.fillPrices('Marco Reus')
#print(price.rare_list)
#price.getMinPrices()
#print(price.min_rare)
#print(price.normal)
