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
        self.go_back(update)
    
    def is_going_to_player(self, update):
        text = update.message.text
        return text.lower()=='show player'
    def on_enter_player(self, update):
        update.message.reply_text("Which player you want to see ?1.Russel 2.Harden 3.Curry 4.Durant 5.Lebron")    
        self.go_back(update)

    def is_going_to_trap(self, update):
        if  self.isPlayer(update.message.text)==True:
            return False
        elif self.isRank(update.message.text)==True:
            return False
        else:
            return True
    def on_enter_trap(self, update):
        update.message.reply_text("Wrong Input......")
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