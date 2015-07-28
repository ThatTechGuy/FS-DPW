class DataTrojan(object):
    __init__(self):
    brief = [
        "This mission is of the utmost importance and will be assigned to you Virgo Squad. Watchdog, your team will be responsible for taking down the SatCom device in Chile. God Speed!",
        "There is no denying the votality this mission will require of you Pisces Squad. Longhorn, you and your team will form the taskforce charged with shutting down the cartel in Russia.",
        "I can't say this mission won't be difficult, but I know the Lebra Squad can handle it! Goodfella, your team will be subjected to a night raid on a drug compound in Mexico.",
        "Alright Cancer Squad, it's times like these we have an opportunity to show our true colors. Quickdraw, we need you and your team to ensure a successful reconicense mission in Latvia.",
        "Taurus Squad, I know you guys have been together for a long time, use that to your advantage here. Spitfire, we need your team to destroy and incapacitate an arms dealer in Iraq."
    ]
    self.__database = [
        ["name","local","squad","leader","brief"],
        ["Alpha","Chile","Virgo","Watchdog",brief[0]],
        ["Beta","Russia","Pisces","Longhorn",brief[1]],
        ["Charlie","Mexico","Lebra","Goodfella",brief[2]],
        ["Delta","Latvia","Cancer","Quickdraw",brief[3]],
        ["Echo","Iraq","Taurus","Spitfire",brief[4]]
    ]


'''
DataTrojan

noparam
Page Array

withparam
name
local
squad
leader
brief
