#!/usr/bin/python3
#
#  /7/7/7
# __|_|_|_o-
#/ /! | |
#\ L'/! |
# \  L' |
#  \___/ Maestraccio

version = "2.2"
date = "20230921"

import os, subprocess, textwrap
from os.path import expanduser
from time import sleep

basismap = os.path.dirname(os.path.realpath(__file__))
os.chdir(basismap)
I     = "\033[7m"
Red   = "\033[31m"
Green = "\033[32m"
Blue  = "\033[94m"
R     = "\033[0m"
uhoh  = "\033[41m\033[93m"
cl = [Red,Blue]
pl = ["Red","Blue"]
nllist = ["NL","HL"]
w = 25

forcen = ("{:^%s}"%w).format
sl = [0,0]
exitlist = ["Q", "X", "QUIT", "EXIT"]
inputindent = "  : "
dot = "."
s = " "
o = "o"
x = "x"
f = "F"
a = "'"
h = "-"
pos = 212
here = Green + o + R
targets = [dot, "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]

grid = [
s,s,s,s,I+Red+s,"D","R","I","B","B","L","E","S","C","R","I","B","B","L","E",s+R,s,s,s,s+"\n",
s,s,"a",s,"b",s,"c",s,"d",s,"e",s,"f",s,"g",s,"h",s,"i",s,"j",s,"k",s,s+"\n",
"+",h,h,h,h,h,h,h,Red+"/"+R,s,dot,s,dot,s,dot,s,Red+"\\"+R,h,h,h,h,h,h,h,"+\n",
"|",s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,"|\n",
"|",s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,"|\n",
"|",s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,"|\n",
"|",s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,"|\n",
"|",s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,"|\n",
"|",s,dot,s,dot,s,dot,s,dot,s,dot,s,here,s,dot,s,dot,s,dot,s,dot,s,dot,s,"|\n",# grid[212]
"|",s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,"|\n",
"|",s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,"|\n",
"|",s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,"|\n",
"|",s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,"|\n",
"|",s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,dot,s,"|\n",
"+",h,h,h,h,h,h,h,Blue+"\\"+R,s,dot,s,dot,s,dot,s,Blue+"/"+R,h,h,h,h,h,h,h,"+\n",
s,s,"a",s,"b",s,"c",s,"d",s,"e",s,"f",s,"g",s,"h",s,"i",s,"j",s,"k",s,s+"\n",
s,s,s,s,I+Blue+s,"D","R","I","B","B","L","E","S","C","R","I","B","B","L","E",s+R,s,s,s,s+"\n"
]

def logo():
    print()
    c = 0
    for i in forcen("D  R  I  B  B  L  E"):
        print(cl[c]+i+R,end = "",flush = True)
        sleep(0.05)
        c += 1
        if c == len(cl):
            c = 0
    print()
    for i in forcen(" S  C  R  I  B  B  L  E"):
        print(cl[c]+i+R,end = "",flush = True)
        sleep(0.05)
        c += 1
        if c == len(cl):
            c = 0
    print()
logo()
print()

kickoff = "Player \"%sRed%s\" kicks off." % (Red,R)
players1 = textwrap.wrap("Flip a coin or a credit card who will be that first player. You can change both PlayerNames in CSV-style (comma-separated, like \"Jane, Joe\"). The first name will replace \"Red\", the second name will replace \"Blue\", or just play as \"Red\" vs \"Blue\", leaving this field blank.",width = w)
print(kickoff)
for i in players1:
    print(i)
playerslike = input(inputindent)
if playerslike.upper() in exitlist:
    exit()
if "," in playerslike:
    pl = []
    plin = playerslike.split(",")[:2]
    for i in plin:
        pl.append(i.strip()[:25])
print()

def showgrid(grid):
    for i in range(len(grid)):
        print(grid[i], end = "", flush = True)
        sleep(0.001)

def alloptions():
    options1 = textwrap.wrap("All keybord input options are located on the middle line of a QWERTY-keyboard from \"A\" to \"G\":",width = w)
    options2 = """%sll keyboard options
%score and position
%sescription and rules
%sree kick
%same save/restore""" % (Green+"a"+R,Green+"s"+R,Green+"d"+R,Green+"f"+R,Green+"g"+R)
    options3 = textwrap.wrap("and to play a move from \"H\" to \"L\" like in Vim:",width = w)
    options4 = """%s       : ← left
%s       : ↓ down
%s       : ↑ up
%s       : → right""" % (Green+"h"+R,Green+"j"+R,Green+"k"+R,Green+"l"+R)
    options5 = textwrap.wrap("These can be preceeded with a back- or forward slash (\"\\\" or \"/\"):",width = w)
    options6 = """%s or %s: ↖ left up
%s or %s: ↙ left down
%s or %s: ↗ right up
%s or %s: ↘ right down""" % (Green+"\\h"+R,Green+"\\k"+R,Green+"/h"+R,Green+"/j"+R,Green+"/k"+R,Green+"/l"+R,Green+"\\j"+R,Green+"\\l"+R)
    options7 = textwrap.wrap("There are some exceptions of course:",width = w)
    options8 = """%s or %s: abort game.""" % (Red+exitlist[0].lower()+R,Red+exitlist[1].lower()+R)
    options9 = textwrap.wrap("Confirm every input with \"Enter\"",width = w)
    for i in options1:
        print(i)
    print(options2)
    for i in options3:
        print(i)
    print(options4)
    for i in options5:
        print(i)
    print(options6)
    for i in options7:
        print(i)
    print(options8)
    for i in options9:
        print(i)
    play = input()
    if play.upper() in exitlist:
        exit()
alloptions()

def score():
    print()
    score = textwrap.wrap("The current score is:",width = w)
    for i in score:
        print(i)
    print(Red+str(int(sl[0]))+R+" - "+Blue+str(int(sl[1]))+R)
    if pos % w == 2:
        plet = "a"
    elif pos % w == 4:
        plet = "b"
    elif pos % w == 6:
        plet = "c"
    elif pos % w == 8:
        plet = "d"
    elif pos % w == 10:
        plet = "e"
    elif pos % w == 12:
        plet = "f"
    elif pos % w == 14:
        plet = "g"
    elif pos % w == 16:
        plet = "h"
    elif pos % w == 18:
        plet = "i"
    elif pos % w == 20:
        plet = "j"
    elif pos % w == 22:
        plet = "k"
    position = textwrap.wrap("It's player %s's turn from a position somewhere on column %s." % (player,plet),width = w)
    for i in position:
        print(i)
    print()

def description():
    logo()
    des1 = textwrap.wrap("is a fun fork of \"Paper soccer\" and was written in memory of Ludo, my respected father, who taught us how to play it with pen and paper.",width = w)
    des2 = textwrap.wrap("Every move (\"dribble\") consists of exactly three steps, drawing lines from free dot to free dot or into the goal, never crossing a line. Type \"a\" for how to move around.",width = w) 
    des3 = textwrap.wrap("POINTS ARE SCORED BY BLOCKING THE OPPONENT.",width = w)
    des4 = textwrap.wrap("When you are cornered by your opponent and cannot make a full three-dot dribble from your current position, you must choose a dot from which YOUR OPPONENT can take a free kick (\"F\").",width = w)
    des5 = textwrap.wrap("YOUR OPPONENT SCORES A POINT NOW!",width = w)
    des6 = textwrap.wrap("The game ends when one of the players hits ANY goal (\"a\"-\"k\"), regardless of the colour. The winner is the player who took the most free kicks, or in case of a score draw, the player that ends the game in any goal.",width = w) 
    fun = " H  A  V  E    F  U  N  !"
    for i in des1:
        print(i)
    for i in des2:
        print(i)
    print(Green,end="")
    for i in des3:
        print(forcen(i))
    print(R,end="")
    for i in des4:
        print(i)
    print(Green,end="")
    for i in des5:
        print(forcen(i))
    print(R,end="")
    for i in des6:
        print(i)
    print()
    c = 0
    for i in forcen(fun):
        print(cl[c]+i+R,end = "",flush = True)
        sleep(0.05)
        c += 1
        if c == len(cl):
            c = 0
    print()
    play = input()
    if play.upper() in exitlist:
        exit()
    if play.lower() == "a":
        alloptions()

def freekick(pos):
    if player == pl[0]:
        m = -1
    else:
        m = 1
    grid[pos] = cl[pl.index(player)-1]+I+"F"+R
    sl[pl.index(player)-1] += 1
    freekick = []
    fkletter = []
    while len(freekick) == 0:
        if pos % w == 2:
            left = pos-2
            plet = "a"
        elif pos % w == 4:
            left = pos-4
            plet = "b"
        elif pos % w == 6:
            left = pos-6
            plet = "c"
        elif pos % w == 8:
            left = pos-8
            plet = "d"
        elif pos % w == 10:
            left = pos-10
            plet = "e"
        elif pos % w == 12:
            left = pos-12
            plet = "f"
        elif pos % w == 14:
            left = pos-14
            plet = "g"
        elif pos % w == 16:
            left = pos-16
            plet = "h"
        elif pos % w == 18:
            left = pos-18
            plet = "i"
        elif pos % w == 20:
            left = pos-20
            plet = "j"
        elif pos % w == 22:
            left = pos-22
            plet = "k"
        for i in range(left,left+w,2):
            if grid[i] in targets:
                freekick.append(i)
        if len(freekick) == 0:
            pos = pos + w * m
    choosedot = textwrap.wrap("Your opponent gets a Free Kick and scores a point. Choose a dot:",width = w)
    for i in choosedot:
        print(i)
    for i in freekick:
        print(" "+grid[(i%w)+w], end = "")
        fkletter.append(grid[(i%w)+w])
    print()
    there = False
    while there == False:
        where = input(inputindent).lower()
        if where.upper() in exitlist:
            exit()
        elif where in fkletter:
            newpos = grid.index(where) - grid.index(plet)
            pos = pos+newpos
            there = True
    return pos

def gameback(grid,num,pos,sl,pl):
    stuff = ["M", "R"]
    filestuffquestion = textwrap.wrap("Do you want to \"M\"ake or \"R\"estore a backup?",width = w)
    gamewriteconfirmed = textwrap.wrap("A backup of the current game was succesfully made. To restore, start a new game and choose \"G\"ame - \"R\"estore.",width = w)
    gameretreiveconfirmed = textwrap.wrap("The backup was succesfully restored.",width = w)
    gamenobackup = textwrap.wrap("No backup file was found on this device.",width = w)
    filename = "Dribblescribblegame.py"
    filestuff = ""
    while filestuff.upper() not in stuff:
        for i in filestuffquestion:
            print(i)
        filestuff = input(inputindent)
        if filestuff.upper() in exitlist:
            exit()
        elif filestuff.upper() == stuff[0]:
            with open(filename, "w") as f:
                print("grid = %s" % (grid),file = f)
                print("num = %d" % (num),file = f)
                print("pos = %d" % (pos),file = f)
                print("sl = %s" % (sl),file = f)
                print("pl = %s" % (pl),file = f)
            for i in gamewriteconfirmed:
                print(i)
            print()
        elif filestuff.upper() == stuff[1]:
            if os.path.isfile(filename):
                from Dribblescribblegame import grid,num,pos,sl,pl
                for i in gameretreiveconfirmed:
                    print(i)
                print()
            else:
                for i in gamenobackup:
                    print(i)
                print()
        else:
            print()
            break
    return grid,num,pos,sl,pl

def move():
    movelist = []
    move = input(cl[i]+player+"\n"+inputindent+R).lower()
    if move.upper() in exitlist:
        movelist.append(exitlist[0])
        return movelist
    if move == "0":
        print("Version: %s\nDate: %s\n" % (version,date))
        movelist.append("0")
        return movelist
    if move.lower() == "a":
        alloptions()
        movelist.append("a")
        return movelist
    if move.lower() == "s":
        score()
        movelist.append("s")
        return movelist
    if move.lower() == "d":
        description()
        movelist.append("d")
        return movelist
    if move.lower() == "f":
        freek = freekick(pos)
        movelist.append("f")
        movelist.append(freek)
        return movelist
    if move.lower() == "g":
        gamebak = gameback(grid,num,pos,sl,pl)
        movelist.append("g")
        movelist.append(gamebak)
        return movelist
    while len(movelist) < 3:
        try:
            if move[0] == "\\":
                if move[1] in ["h","k"]:
                    movel = -27
                    movelist.append(movel)
                    move = move[2:]
                elif move[1] in ["j","l"]:
                    movel = 27
                    movelist.append(movel)
                    move = move[2:]
                else:
                    move = move[1:]
            elif move[0] == "/":
                if move[1] in ["h","j"]:
                    movel = 23
                    movelist.append(movel)
                    move = move[2:]
                elif move[1] in ["k","l"]:
                    movel = -23
                    movelist.append(movel)
                    move = move[2:]
                else:
                    move = move[1:]
            elif move[0] == "h":
                movel = -2
                movelist.append(movel)
                move = move[1:]
            elif move[0] == "j":
                movel = 25
                movelist.append(movel)
                move = move[1:]
            elif move[0] == "k":
                movel = -25
                movelist.append(movel)
                move = move[1:]
            elif move[0] == "l":
                movel = 2
                movelist.append(movel)
                move = move[1:]
            else:
                move = move[1:]
        except:
            return movelist
    return movelist

game = True
while game == True:
    for i in range(len(cl)):
        movie = False
        while movie == False:
            showgrid(grid)
            player = pl[i]
            num = i
            movelist = move()
            if len(movelist) == 1 and movelist[0] == exitlist[0]:
                exit()
            posorg = pos
            if len(movelist) == 3:
                mo = 0
                for j in movelist:
                    good = True
                    aim = pos + j
                    if grid[aim] not in targets:
                        good = False
                    if j == -27 and grid[pos-1] != s:
                        good = False
                    elif j == -23 and grid[pos+1] != s:
                        good = False
                    elif j == 23 and grid[pos+24] != s:
                        good = False
                    elif j == 27 and grid[pos+26] != s:
                        good = False
                    if good == False:
                        break
                    pos = aim
                pos = posorg
                done = False
                if good == True:
                    grid[pos] = cl[i]+x+R
                    for j in movelist:
                        if j == -27:
                            ar = cl[i]+"\\"+R
                            grid[pos-1] = cl[i]+a+R
                        elif j == -25:
                            ar = cl[i]+"|"+R
                        elif j == -23:
                            ar = cl[i]+"/"+R
                            grid[pos+1] = cl[i]+a+R
                        elif j == 2:
                            ar = cl[i]+"-"+R
                        elif j == 27:
                            ar = cl[i]+"\\"+R
                            grid[pos+26] = cl[i]+a+R
                        elif j == 25:
                            ar = cl[i]+"|"+R
                        elif j == 23:
                            ar = cl[i]+"/"+R
                            grid[pos+24] = cl[i]+a+R
                        elif j == -2:
                            ar = cl[i]+"-"+R
#                        if j == -27:
#                            ar = cl[i]+"↖"+R
#                            grid[pos-1] = cl[i]+a+R
#                        elif j == -25:
#                            ar = cl[i]+"↑"+R
#                        elif j == -23:
#                            ar = cl[i]+"↗"+R
#                            grid[pos+1] = cl[i]+a+R
#                        elif j == 2:
#                            ar = cl[i]+"→"+R
#                        elif j == 27:
#                            ar = cl[i]+"↘"+R
#                            grid[pos+26] = cl[i]+a+R
#                        elif j == 25:
#                            ar = cl[i]+"↓"+R
#                        elif j == 23:
#                            ar = cl[i]+"↙"+R
#                            grid[pos+24] = cl[i]+a+R
#                        elif j == -2:
#                            ar = cl[i]+"←"+R
                        aim = pos + j
                        if grid[aim] in targets:
                            if grid[aim] in targets[1:]:
                                here = I+here+R
                                grid[aim-1] = I+Green+" "+R
                                grid[aim+1] = I+Green+" "+R
                                done = True
                            if mo == 2:
                                ar = here
                            grid[aim] = ar
                            pos = aim
                            mo += 1
                            movie = True 
                        else:
                            print(uhoh+forcen("Illegal move!")+R)
                            print()
                    if done == True:
                        print()
                        print(cl[i]+forcen(player+" ends the game")+R)
                        sl[pl.index(player)] += 0.5
                        wp = pl[sl.index(max(sl))]
                        ws = int(max(sl))
                        wc = cl[sl.index(max(sl))]
                        lc = cl[sl.index(max(sl))-1]
                        ls = int(sl[sl.index(max(sl))-1])
                        print(wc+wp+R)
                        print(forcen("wins the game with"))
                        print(Red+str(int(sl[0]))+R+" - "+Blue+str(int(sl[1]))+R)
                        showgrid(grid)
                        exit()
                else:
                    print(uhoh+forcen("Illegal move!")+R)
                    print()
            elif len(movelist) == 2 and movelist[0] == "f":
                pos = movelist[1]
                grid[pos] = here
                movie = True
            elif len(movelist) == 2 and movelist[0] == "g":
                grid = movelist[1][0]
                num = movelist[1][1]
                pos = movelist[1][2]
                sl = movelist[1][3]
                pl = movelist[1][4]
                playerr = pl[num]
                if playerr == player:
                    movie = False
                else:
                    movie = True
            elif len(movelist) == 1 and movelist[0] in ["0","a","s","d"]:
                pass
            else:
                print(uhoh+forcen("Illegal move!")+R)
                print()

