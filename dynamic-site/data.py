class DataTrojan(object):
    def __init__(self):
    #Initiate class with a database made up of two inter-dependent tables
        brief = [
            "This mission is of the utmost importance and will be assigned to you Virgo Squad. Watchdog, your team will be responsible for taking down the SatCom device in Chile. God Speed!",
            "There is no denying the volatility of this mission or what it will require Pisces Squad. Longhorn, your team will form the taskforce charged with shutting down the cartel in Russia.",
            "I can't say this mission won't be difficult, but I know the Lebra Squad can handle it! Goodfella, your team will be subjected to a night raid on a drug compound in Mexico.",
            "Alright Cancer Squad, it's times like these we have an opportunity to show our true colors. Quickdraw, we need you and your team to ensure a successful reconicense mission in Latvia.",
            "Taurus Squad, I know you guys have been together for a long time, use that to your advantage here. Spitfire, we need your team to destroy and incapacitate an arms dealer in Iraq."
        ]
        self.__database = [
            ["name","local","squad","leader","brief"],
            ["Alpha","Chile","Virgo","Watchdog",brief[0]],
            ["Bravo","Russia","Pisces","Longhorn",brief[1]],
            ["Charlie","Mexico","Lebra","Goodfella",brief[2]],
            ["Delta","Latvia","Cancer","Quickdraw",brief[3]],
            ["Echo","Iraq","Taurus","Spitfire",brief[4]]
        ]

    #GETTER that cycles through the database and returns the operation names
    @property
    def data(self):
        op_names = []
        for ops in self.__database:
            op_names.append(ops[0])
        del op_names[0]
        return op_names

    #Method that takes the key to find the row requested in the db and returns as object
    def auth(self, op):
        op_data = {}
        search = (ops for ops in self.__database if ops[0] == op).next()
        i = 0
        for key in self.__database[0]:
            op_data[key] = search[i]
            i += 1
        return op_data
