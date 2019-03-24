from autocklicker import *
from futbin import *
from player_file import *


bot   = AutoClicker()
playerlist = PLAYERLIST()

#bot.suche_pic_two_click(bot.kaufen, bot.nicht_bekommen, 500)

#price.calculatePrices('Fabio Quagliarella', 'gold')


for i in range(0,4):
    for from_player_list in playerlist.playerlist:
        price       = FUTBIN()
        player      = from_player_list[0]
        quality     = from_player_list[1]
        sell_amount = from_player_list[2]

        price.calculatePrices(player, quality)
        if price.time < 20 and price.verkauf > 0 and sell_amount < 1:
            bot.fill_suchmaske(player, quality,  price.einkauf, 150)
            proof = bot.part_suchen()
            if proof == 'gekauft':
                bot.part_verkaufen(price.verkauf)
                bot.push_zurueck()

                ## count sells
                from_player_list[2] = from_player_list[2] + 1
                playerlist.save_player_file(playerlist.playerlist)

            elif proof == 'nicht bekommen':
                bot.push_zurueck()


