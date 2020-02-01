# -*- coding: utf-8 -*-
"""
Created on Wed Jan 8 12:01:26 2020

@author: dbowder
"""
import Dominion
import random
from collections import defaultdict
import testUtility

#Get player names
player_names = ["User","*Computer1","*Computer2"]

#number of curses and victory cards
nV, nC = testUtility.GetnVnC(player_names)

#Define box
box = testUtility.GetBoxes(nV)
supply_order = testUtility.GetSupplyOrder()

#Pick 10 cards from box to be in the supply.
boxlist = [k for k in box]
random.shuffle(boxlist)
random10 = boxlist[:10]
supply = defaultdict(list,[(k,box[k]) for k in random10])
supply = testUtility.GetSupply(player_names, supply, nV, nC)

#initialize the trash
trash = []

#Costruct the Player objects
players = testUtility.GetPlayers(player_names)


# Bug 2: Workshop behaves like a Village
box["Workshop"]=[Dominion.Village()]*10


#Play the game
turn  = 0
while not Dominion.gameover(supply):
    turn += 1
    print("\r")
    for value in supply_order:
        print (value)
        for stack in supply_order[value]:
            if stack in supply:
                print (stack, len(supply[stack]))
    print("\r")
    for player in players:
        print (player.name,player.calcpoints())
    print ("\rStart of turn " + str(turn))
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players,supply,trash)


#Final score
dcs=Dominion.cardsummaries(players)
vp=dcs.loc['VICTORY POINTS']
vpmax=vp.max()
winners=[]
for i in vp.index:
    if vp.loc[i]==vpmax:
        winners.append(i)
if len(winners)>1:
    winstring= ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0],'wins!'])

print("\nGAME OVER!!!\n"+winstring+"\n")
print(dcs)
