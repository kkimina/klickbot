from numpy import *
import os.path
import pickle
class PLAYERLIST():

    def __init__(self):
        self.playerlist = []
        if os.path.exists('myfile.pkl'):
            self.get_player_file()
        else:
            self.create_playerlist()

    def create_playerlist(self):
        self.playerlist.append(['Marco Reus'          , 'gold', 0])
        self.playerlist.append(['Portu'               , 'gold', 0])
        self.playerlist.append(['Portu'               , 'spezial', 0])
        self.playerlist.append(['Max Kruse'           , 'gold'  , 0])
        self.playerlist.append(['Max Kruse'           , 'spezial', 0])
        self.playerlist.append(['Richarlison'         , 'gold'  , 0])
        self.playerlist.append(['Richarlison'         , 'spezial', 0])
        self.playerlist.append(['Vieirinha'           , 'spezial', 0])
        self.playerlist.append(['Regis Gurtner'       , 'spezial', 0])
        self.playerlist.append(['Hamdallah'           , 'spezial', 0])
        self.playerlist.append(['Wout Weghorst'       , 'spezial', 0])
        self.playerlist.append(['Albin Ekdal'         , 'spezial', 0])
        self.playerlist.append(['Romain Hamouma'      , 'spezial', 0])
        self.playerlist.append(['John McGinn'         , 'spezial', 0])
        self.playerlist.append(['Fabio Quagliarella'  , 'spezial', 0])
        self.playerlist.append(['Stuani'              , 'spezial', 0])
        self.playerlist.append(['Fabian Schar'        , 'spezial', 0])
        self.playerlist.append(['Robin van Persie'    , 'spezial', 0])
        self.playerlist.append(['Morata'              , 'spezial', 0])
        self.playerlist.append(['Camilo Vargas'       , 'spezial', 0])
        self.playerlist.append(['Filip Kostic'        , 'spezial', 0])
        self.playerlist.append(['Flavien Tait'        , 'spezial', 0])
        self.playerlist.append(['Marcus Maddison'     , 'spezial', 0])
        self.playerlist.append(['Nicolas Pallois'     , 'spezial', 0])
        self.playerlist.append(['Kenneth Vermeer'     , 'spezial', 0])
        self.playerlist.append(['Angel Mena'          , 'spezial', 0])
        self.playerlist.append(['Deulofeu'            , 'spezial', 0])
        self.playerlist.append(['James Tarkowski'     , 'spezial', 0])       
        self.playerlist.append(['Jadon Sancho'        , 'spezial', 0])       
        #self.playerlist.append(['Marco Verratti', 'spezial'])               
        self.playerlist.append(['Michail Antonio'     , 'spezial', 0])       
        self.playerlist.append(['Luka Jovic'          , 'spezial', 0])       
        self.playerlist.append(['Samu Castillejo'     , 'spezial', 0])       
        self.playerlist.append(['Nabil Fekir'         , 'gold', 0])          
        self.playerlist.append(['Camilo Vargas'       , 'gold', 1])          
        #self.playerlist.append(['Hyun Soo Hwang'      , 'spezial'])         

    def save_player_file(self, list):
        output = open('myfile.pkl', 'wb')
        pickle.dump(list, output)
        output.close()

    def get_player_file(self):
        self.playerlist = []
        pkl_file = open('myfile.pkl', 'rb')
        self.playerlist = pickle.load(pkl_file)
        pkl_file.close()

