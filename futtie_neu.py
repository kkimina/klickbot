import sys
from core import CORE
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



def ablauf():
	os.system('clear')
	bot = CORE()
	bot.init(account = 'xxx@hotmail.de', passwort = 'xxx', platform = 'xbox', key = 'kaiee')
	bot.connect()
	bot.getGewinnFromFile()
	bot.getGewinnAndCoins()
	bot.initGui()
	bot.refreshGewinn()
	bot.refreshCoins()

ablauf()

# Code to add widgets will go here...


