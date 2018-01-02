from transitions.extensions import GraphMachine


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )

    def is_going_to_greeting(self, update):
        text = update.message.text
        return True
    def on_enter_greeting(self, update):
        update.message.reply_text("Hello nice to meet you\nI am a nba guide tour bot\nI can show you player or nba team rank")   

    def is_going_to_rank(self, update):
        text = update.message.text
        return text.lower()=='show rank of team'
    
    def on_enter_rank(self, update):
        update.message.reply_text("Which one you want to see ? Eastern team rank or Western team rank?")    
        
    
    def is_going_to_player(self, update):
        text = update.message.text
        return text.lower()=='show player'
    def on_enter_player(self, update):
        update.message.reply_text("Which player you want to see ?\n1.Russel Westbrook\n2.James Harden\n3.Lebron James\n4.Anthony Davis\n5.Kawhi Leonard")    
        
    def is_going_to_showPlayer(self,update):
        text=update.message.text
        return self.isRealPlayer(update.message.text)
    def on_enter_showPlayer(self, update):
        if update.message.text.lower()=='russel westbrook':
            update.message.reply_text("31.6 pts 10.7 rebs 10.4 ast 2 stl 0.1 blk\n42.5% 34.3% 84.5%")
            update.message.reply_photo(open("img/westbrook.jpg","rb"))
        elif update.message.text.lower()=='james harden':
            update.message.reply_text("29.1 pts 8.2 rebs 11.2 ast 1.4 stl 0.4 blk\n44.0% 34.7% 84.7%")
            update.message.reply_photo(open("img/harden.jpg","rb"))
        elif update.message.text.lower()=='lebron james':
            update.message.reply_text("26.4 pts 8.6 rebs 8.7 ast 1.2 stl 0.5 blk\n54.8% 36.3% 67.4%")
            update.message.reply_photo(open("img/lebron.jpg","rb"))
        elif update.message.text.lower()=='anthony davis': 
            update.message.reply_text("28.0 pts 11.8 rebs 2.1 ast 1.2 stl 2.2 blk\n50.5% 29.9% 80.2%")
            update.message.reply_photo(open("img/davis.jpg","rb"))  
        elif update.message.text.lower()=='kawhi leonard':
            update.message.reply_text("25.5 pts 5.8 rebs 3.5 ast 1.8 stl 0.7 blk\n48.5% 38% 88%")
            update.message.reply_photo(open("img/leonard.jpg","rb"))
        self.go_back(update)             
    def is_going_to_showEast(self, update):
        text = update.message.text
        return text.lower()=='eastern team'
    
    def on_enter_showEast(self, update):
        update.message.reply_photo(open("img/east.jpg","rb"))
        update.message.reply_text("1.Boston 53W 29L\n2.Cleveland 51W 31L\n3.Toronto 51W 31L\n4.Washington 49W 33L\n5.Atlanta 43W39L\n6.Milwaukee 42W 40L\n7.Indiana 42W 40L\n8.Chicago 41W 41L")    
        self.go_back(update)

    def is_going_to_showWest(self, update):
        text = update.message.text
        return text.lower()=='western team'
    
    def on_enter_showWest(self, update):
        update.message.reply_photo(open("img/west.jpg","rb"))
        update.message.reply_text("1.Golden State 67W 15L\n2.San Antonio 61W 21L\n3.Houston 55W 27L\n4.LA 51W 31L\n5.Utah 51W 31L\n6.Oklahoma City 47W 35L\n7.Memphis 43W 39L\n8.Portland 41W 41L\n")    
        self.go_back(update)        


    def is_going_to_trap(self, update):
        if  self.isPlayer(update.message.text)==True:
            return False
        elif self.isRank(update.message.text)==True:
            return False
        elif self.isTeam(update.message.text)==True:
            return False
        elif self.isRealPlayer(update.message.text)==True:
            return False
        else:
            return True
    def on_enter_trap(self, update):
        update.message.reply_text("Wrong Input......")
        self.go_back(update)    
    
    def is_going_to_trap2(self, update):
        if self.isTeam(update.message.text)==True:
            return False
        else:
            return True
    def on_enter_trap2(self, update):
        update.message.reply_text("Wrong input format you should input Eastern team or Western team")
        self.go_back(update)    
        

    def is_going_to_trap3(self, update):
        if self.isRealPlayer(update.message.text)==True:
            return False
        else:
            return True
    def on_enter_trap3(self, update):
        update.message.reply_text("Type wrong name you should type again")
        self.go_back(update)       


    def on_exit_state1(self, update):
        print('Leaving state1')

    

    def on_exit_state2(self, update):
        print('Leaving state2')

    def isPlayer(self,str):
        if str.lower()=='show player':
            return True
        else :
            return False
    def isRank(self,str):
        if str.lower()=='show rank':
            return True
        else :
            return False

    def isTeam(self,str):
        if str.lower()=='western team':
            return True
        elif str.lower()=='eastern team':
            return True
        else:
            return False

    def isRealPlayer(self,str):
        if str.lower()=='russel westbrook':
            return True
        elif str.lower()=='james harden':
            return True
        elif str.lower()=='lebron james':
            return True
        elif str.lower()=='kawhi leonard':
            return True
        elif str.lower()=='anthony davis':
            return True
        else :
            return False   

        