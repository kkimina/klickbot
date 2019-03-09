import fut
import json
import time
import random
import os
from pprint import pprint
import requests

IF      = 'IF'
TOTGS   = 'TOTGS'
CL      = 'CL'
NORMAL  = 'Normal'
SWAP    = 'Swap Deal Reward SBC'
POTM = 'Bundes POTM'
SIF = 'SIF'
UCL = 'UCL LIVE'
HALLOWEEN = 'Halloween'
OTW = 'OTW'


class FUTBIN:
    rare_list   = {}
    normal_list = {}
    min_rare    = 0
    normal      = 0

    def fillPrices(self, name):
        try:
            output = requests.get('https://www.futbin.com/search?year=19&extra=1&term='+str(name)).text
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
                    self.rare_list[s['version']] = int(sum)
        except:
            print('error by ' + name)
            self.fillPrices(name)

    def getMinPrices(self):
        for h in self.rare_list.keys():
            if h == 'Normal':
                self.normal = self.rare_list[h]
            else:
                if h != 'Winter Refresh':
                    if self.min_rare == 0 and self.rare_list[h] != 0:
                        self.min_rare = self.rare_list[h]
                    else:
                        if self.rare_list[h] < self.min_rare:
                            self.min_rare = self.rare_list[h]




price = FUTBIN()
price.fillPrices('Marco Reus')
print(price.rare_list)
price.getMinPrices()
print(price.min_rare)
print(price.normal)
