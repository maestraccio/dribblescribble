#!/usr/bin/python3
#
#  /7/7/7
# __|_|_|_o-
#/ /! | |
#\ L'/! |
# \  L' |
#  \___/ Maestraccio

version = "1.1"
date = "20230115"

import os
import subprocess
from os.path import expanduser
from time import sleep

I     = "\033[7m"
Red   = "\033[31m"
Green = "\033[32m"
Blue  = "\033[94m"
R     = "\033[0m"
pl = [Blue,Red]
nllist = ["NL","HL"]

forcen = "{:^25}"
sl = [Blue + "'" + R,Red + "'" + R]
exitlist = ["Q", "X", "QUIT", "EXIT"]
inputindent = "\n  : "
dot = "."
s = " "
o = "o"
x = "x"
f = "#"
a = "'"
h = "-"
pos = 220
here = Green + o + R
targets = [dot, "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k"]
grid = [
        s, s, s, s, s, I + Red + "D", "R", "I", "B", "B", "L", "E", "S", "C", "R", "I", "B", "B", "L", "E" + R, s, s, s, s, s, "\n",
        s, s, "a", s, "b", s, "c", s, "d", s, "e", s, "f", s, "g", s, "h", s, "i", s, "j", s, "k", s, s, "\n",
        "+", h, h, h, h, h, h, h, Red + "/" + R, s, dot, s, dot, s, dot, s, Red + "\\" + R, h, h, h, h, h, h, h, "+", "\n",
        "|", s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, "|", "\n",
        "|", s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, "|", "\n",
        "|", s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, "|", "\n",
        "|", s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, "|", "\n",
        "|", s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, "|", "\n",
        "|", s, dot, s, dot, s, dot, s, dot, s, dot, s, here, s, dot, s, dot, s, dot, s, dot, s, dot, s, "|", "\n",   # pos = grid[220]
        "|", s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, "|", "\n",
        "|", s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, "|", "\n",
        "|", s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, "|", "\n",
        "|", s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, "|", "\n",
        "|", s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, dot, s, "|", "\n",
        "+", h, h, h, h, h, h, h, Blue + "\\" + R, s, dot, s, dot, s, dot, s, Blue + "/" + R, h, h, h ,h , h, h , h, "+", "\n",
        s, s, "a", s, "b", s, "c", s, "d", s, "e", s, "f", s, "g", s, "h", s, "i", s, "j", s, "k", s, s, "\n",
        s, s, s, s, s, I + Blue + "D", "R", "I", "B", "B", "L", "E", "S", "C", "R", "I", "B", "B", "L", "E" + R, s, s, s, s, s, "\n",
        ]
ml = ["h","l","k","j","\\h","\\k","/h","/j","/l","/k","\\l","\\j","w","o","n","z","\\w","\\n","/w","/z","/o","/n","\\o","\\z"]
dribblescribble = forcen.format("DRIBBLESCRIBBLE")
langvraag = """
Kies \"NL\" voor Nederlands
Else play in English"""
lang = input(langvraag + inputindent)
if lang.upper() in nllist:
    intro = """
is geschreven met mijn
gerespecteerde vader Ludo
in gedachten, die ons
leerde het te spelen met
pen en papier.
Het is een leuke variant
op \"Paper Soccer\".

Iedere beurt (\"dribble\")
bestaat uit precies drie
bewegingen, dmv. het
tekenen van lijnen van
stip naar stip of in het
doel, waarbij je nooit
een lijn mag kruisen. Je
verzamelt punten door je
opponent vast te zetten
zodat die geen drie vrije
punten meer kan bereiken.
Als je geblokkeerd bent
moet je de %stegenstander%s
een %svrije trap%s toekennen
met \"f\", vanaf een vrij
punt op dezelfde lijn, of
anders een lijn dichter
bij een doel.
%s Je tegenstander scoort
      nu een punt!       %s
Het spel eindigt wanneer
een doel is bereikt (\"d\"-
\"h\"); de %swinnaar%s is
degene die de %smeeste
vrije trappen%s heeft
genomen, of bij gelijk-
spel, degene die het
eerst in het doel scoort,
om het even aan welke
kant.""" % (Green, R, Green, R, I + Green, R, Green, R, Green, R)
    enjoy = "%s%s" % (I,Green)+forcen.format("Veel plezier!")+"%s" % (R)
    welcome = forcen.format("Welkom bij")
    preintro = """

Om alle toetsinputopties
te zien, kies \"a\",
afbreken met \"q\".  Om je
dribble of optiekeuze te
bevestigen, druk op
\"Enter\"."""
    movequestion = """
Jouw zet of optiekeuze
(\"a\" voor alle opties):"""
    possibleoptions = """
Alle toetsinputopties
bevinden zich op de
middelste regel van een
QWERTY-toetsenbord, van
\"A\" t/m \"G\":

%s ll key input options
  (alle toetsinputopties)
%s core and position
  (score en positie)
%s escription and rules
  (spelregels)
%s ree kick
  (vrije trap)
%s ame backup
  (opslaan en ophalen)

en om te zetten van \"H\"
t/m \"L\", zoals in Vim:
%s (%sest)  ← links
  (%sazerswoude)
%s (%suid)  ↓ omlaag
  (%saarsveld)
%s (%soord) ↑ omhoog
  (%sortenhoef)
%s (%sost)  → rechts
  (%seusden)

daar mag een \"\\\" of
\"/\" aan voorafgaan:
%s of %s (%s of %s)
 ↖ links omhoog
%s of %s (%s of %s)
 ↙ links omlaag
%s of %s (%s of %s)
 ↗ rechts omhoog
%s of %s (%s of %s)
 ↘ rechts omlaag

voorbeeld:
\"\\jl/k\" of \"\\zo/n\"
geeft \"↘ → ↗\"

En natuurlijk wat
uitzonderingen:
%s of %s: stoppen""" % (Green +  "a" + R, Green +  "s" + R, Green +  "d" + R, Green +  "f" + R, Green +  "g" + R, Green + ml[0] + R, Green + ml[12] + R, Green + ml[0].upper() + R, Green + ml[3] + R, Green + ml[15] + R, Green + ml[3].upper() + R, Green + ml[2] + R, Green + ml[14] + R, Green + ml[2].upper() + R, Green + ml[1] + R, Green + ml[13] + R, Green + ml[1].upper() + R, Green + ml[4] + R, Green + ml[5] + R, Green + ml[16] + R, Green + ml[17] + R, Green + ml[6] + R, Green + ml[7] + R, Green + ml[18] + R, Green + ml[19] + R, Green + ml[8] + R, Green + ml[9] + R, Green + ml[20] + R, Green + ml[21] + R, Green + ml[10] + R, Green + ml[11] + R, Green + ml[22] + R, Green + ml[23] + R, Red +  exitlist[0].lower() + R, Red + exitlist[1].lower() + R)
    illegalmove = Red + "Ongeldige zet." + R
    owntrail = Red + "Ongeldige zet: je ging\nterug op je eigen spoor." + R
    occupied = Red + "Ongeldige zet: één of\nmeer gekozen posities\nzijn al bezet." + R
    illegalpos = Red + "Ongeldige positie." + R
    choosepos = "Geef je tegenstander een\nvrije strap vanaf een\nnieuwe positie. Kies een\nletter uit de lijst:\n"
    scores = "\n%s scoort een punt!"
    score = "De huidige score is %s-%s"
    gameend = "%s beëindigt het spel."
    winner = "Het scoreboard (%s-%s)\ngeeft aan dat %s de\nwinnaar van dit spel is.\n"
    draw = "De score is gelijk\n(%s-%s), %s wint.\n"
    nowinner = "Het is gelijkspel\n(%s-%s) en dus heeft\nniemand verloren.\n"
    nomoref = "Er zijn geen geldige\nzetten meer."
    stuff = ["O", "S", "A"]
    filestuffquestion = """
Wil je het huidige spel
%schrijven naar een
backupbestand of een
opgeslagen spel %sphalen
(of %snnuleren)?""" % (Green + stuff[1] + R, Green + stuff[0] + R, Green + stuff[2] + R)
    gamewriteconfirmed = "\nDe backup van het spel\nis succesvol geschreven.\n"
    gameretreiveconfirmed = "\nDe backup van het spel\nis succesvol ophehaald.\n"
    gamenobackup = "\nGeen backup gevonden.\n"
    systemerror = "Er is een lees- of\nschrijffout opgetreden:\nMogelijk ondersteunt je\napparaat deze optie niet."
    colpos = """
en jouw p%ssitie is
ergens in kolom \"%s\".
"""
    blue = "Blauw"
    red= "Rood"
    freekicklist1 = "Kies een letter uit"
    freekicklist2 = "voor een vrije trap:\n  : "
else:
    intro = """
was written in memory of
Ludo, my respected father
who taught us how to play
it with pen and paper.
It is a fun variant of
\"Paper soccer\".

Every move (\"dribble\")
consists of exactly three
steps, drawing lines from
free dot to free dot or
into the goal, never
crossing a line. You
collect points by
blocking your opponent.
When you're stuck and
cannot make a full
dribble from your current
position, you must choose
a dot on the same line
for %syour opponent%s to take
a %sfree kick%s (\"f\") from,
or if there isn't one
left free, one on a line
closer to a goal.
%s   Your opponent scores
      a point now!       %s
The game ends when a goal
(\"d\"-\"h\") is reached, the
%swinner%s is the one who
gets the %smost free kicks%s,
or in case of a score
draw, the player that
scores into a goal first
(on any side).
""" % (Green, R, Green, R, I + Green, R, Green, R, Green, R)
    enjoy = "%s%s" % (I,Green)+forcen.format("Have fun!")+"%s%s" % (R,"\n")
    welcome = "\nWelcome to "
    preintro = """
To show all keyboard
input options, choose
\"a\", abort with \"q\".
To confirm your dribble
or option choice, press
\"Enter\"."""
    movequestion = """
Your dribble or menu
choice (\"a\" for all
options):"""
    possibleoptions = """
All keybord input options
are located on the middle
line of a QWERTY-keyboard
from \"A\" to \"G\":

%s ll keyboard options
%s core and position
%s escription and rules
%s ree kick
%s ame save/restore

and to play a move from
\"H\" to \"L\" like in Vim:
%s (or %s)  ← left
 (%sest  = %sazerswoude)
%s (or %s)  ↓ down
 (%suid  = %saarsveld)
%s (or %s)  ↑ up
 (%soord = %sortenhoef)
%s (or %s)  → right
 (%sost  = %seusden)

maybe preceeded with \"\\\"
or \"/\":
%s or %s (%s or %s)
 ↖ left up
%s or %s (%s or %s)
 ↙ left down
%s or %s (%s or %s)
 ↗ right up
%s or %s (%s or %s)
 ↘ right down

example:
\"\\jl/k\" or \"\\zo/n\"
gives \"↘ → ↗\"

And some exceptions of
course:
%s or %s: abort game
""" % (Green +  "a" + R, Green +  "s" + R, Green +  "d" + R, Green +  "f" + R, Green +  "g" + R, Green + ml[0] + R, Green + ml[12] + R, Green + "W" + R, Green + ml[0].upper() + R, Green + ml[3] + R, Green + ml[15] + R, Green + "Z" + R, Green + ml[3].upper() + R, Green + ml[2] + R, Green + ml[14] + R, Green + "N" + R, Green + ml[2].upper() + R, Green + ml[1] + R, Green + ml[13] + R, Green + "O" + R, Green + ml[1].upper() + R, Green + ml[4] + R, Green + ml[5] + R, Green + ml[16] + R, Green + ml[17] + R, Green + ml[6] + R, Green + ml[7] + R, Green + ml[18] + R, Green + ml[19] + R, Green + ml[8] + R, Green + ml[9] + R, Green + ml[20] + R, Green + ml[21] + R, Green + ml[10] + R, Green + ml[11] + R, Green + ml[22] + R, Green + ml[23] + R, Red +  exitlist[0].lower() + R, Red + exitlist[1].lower() + R)
    illegalmove = Red + "Illegal move." + R
    owntrail = Red + "Illegal move: You went\nback on your own trail." + R
    occupied = Red + "Illegal move: One or more\nchosen positions may\nalready be occupied." + R
    illegalpos = Red + "Illegal position." + R
    choosepos = "For an opponent's free\nkick from a new position,\nchoose a letter from the\nfollowing list:\n"
    scores = "\n%s scores one point!"
    score = "The score is: %s-%s"
    gameend = "%s ends the game."
    winner = "The scoreboard (%s-%s)\nindicates %s as the\nwinner of the game.\n"
    draw = "As there is a draw\n(%s-%s), the winner is\n%s.\n"
    nowinner = "As there is a draw (%s-%s),\nthere is no winner.\n"
    nomoref = "There are no more\npossible moves."
    stuff = ["R", "W", "C"]
    filestuffquestion = """
Do you want to %srite
your current game status
to a backup file or
%setreive a previously
saved game (or %sancel)?""" % (Green + stuff[1] + R, Green + stuff[0] + R, Green + stuff[2] + R)
    gamewriteconfirmed = "\nThe backup of your\ncurrent game has been\nsuccesfully written.\n"
    gameretreiveconfirmed = "\nThe game backup was\nsuccesfully retreived.\n"
    gamenobackup = "\nSorry, no backup file was\nfound on this device.\n"
    systemerror = "A file read-write error\noccurred: Your device may\nnot be compatible with\nthis option."
    colpos = """
and your p%ssition is
somewhere on column \"%s\".
"""
    blue = "Blue"
    red= "Red"
    freekicklist1 = "Choose a letter from"
    freekicklist2 = "to take a free kick:\n  : "

print()
print(welcome)
print()

for i in range(len(dribblescribble)):
    print(I + Green + dribblescribble[i] + R, end = "", flush = True)
    sleep(0.05)
print(preintro)

print()
for i in range(len(grid)):
    print(grid[i], end = "", flush = True)
    sleep(0.005)
print()
bf = []
rf = []
print(score % (Blue + str(len(bf)) + R, Red + str(len(rf)) + R))
print()
print(enjoy)

player = pl[0]
while player in pl:
    moveinput = input(player+movequestion+R + inputindent).replace(" ", "").replace("h", " h").replace("j", " j").replace("k", " k").replace("l", " l").replace("w", " w").replace("z", " z").replace("n", " n").replace("o", " o").replace("/", " /").replace("\\", " \\").replace("/ ", "/").replace("\\ ", "\\")
    move = " ".join(moveinput.split())
    spacecount = 0
    for i in move:
        if i == " ":
            spacecount = spacecount + 1
    if move.upper() in exitlist:
        exit()
    elif move.upper() == "D":
        print()
        for i in range(len(dribblescribble)):
            print(I + Green + dribblescribble[i] + R, end = "", flush = True)
            sleep(0.05)
        print(intro)
    elif move.upper() == "A":
        print(possibleoptions)
    elif move.upper() == "S":
        print()
        print(score % (Blue + str(len(bf)) + R, Red + str(len(rf)) + R), end = "")
        if (pos - 2) % 26 == 0:
            print(colpos % (Green + o + R, "a"))
        elif (pos - 4) % 26 == 0:
            print(colpos % (Green + o + R, "b"))
        elif (pos - 6) % 26 == 0:
            print(colpos % (Green + o + R, "c"))
        elif (pos - 8) % 26 == 0:
            print(colpos % (Green + o + R, "d"))
        elif (pos - 10) % 26 == 0:
            print(colpos % (Green + o + R, "e"))
        elif (pos - 12) % 26 == 0:
            print(colpos % (Green + o + R, "f"))
        elif (pos - 14) % 26 == 0:
            print(colpos % (Green + o + R, "g"))
        elif (pos - 16) % 26 == 0:
            print(colpos % (Green + o + R, "h"))
        elif (pos - 18) % 26 == 0:
            print(colpos % (Green + o + R, "i"))
        elif (pos - 20) % 26 == 0:
            print(colpos % (Green + o + R, "j"))
        elif (pos - 22) % 26 == 0:
            print(colpos % (Green + o + R, "k"))
        for i in grid:
            print(i, end = "")
        print()
    elif move.upper() == "G":
        try:
            folder = ""
            filename = "Dribblescribblegame.py"
            filestuff = ""
            while filestuff.upper() not in stuff:
                filestuff = input(filestuffquestion + inputindent)
                if filestuff.upper() == stuff[0]:
                    if os.path.isfile(folder + filename):
                        from Dribblescribblegame import grid, pos, player, bf, rf
                        print(gameretreiveconfirmed)
                        print()
                        for i in grid:
                            print(i, end = "")
                        print()
                    else:
                        print(gamenobackup)
                elif filestuff.upper() == stuff[1]:
                    if os.path.isfile(folder + filename):
                        os.remove(folder + filename)
                    f = open(str(folder + filename),"a")
                    f.write("grid = %s\n" % (grid))
                    f.write("player = \"%s\"\n" % (player))
                    f.write("pos = %d\n" % (pos))
                    f.write("bf = %s\n" % (bf))
                    f.write("rf = %s\n" % (rf))
                    f.close()
                    print(gamewriteconfirmed)
                elif filestuff.upper() == stuff[2] or filestuff.upper() in exitlist:
                    break
        except:
            print(systemerror)
    elif move.upper() == "F":
        player = pl[pl.index(player) - 1]
        if player == Blue:
            print(scores % (Blue + blue + R))
            bf.append(1)
            col = Red
        else:
            print(scores % (Red + red + R))
            rf.append(1)
            col = Blue
        print()
        print(score % (Blue + str(len(bf)) + R,Red + str(len(rf)) + R))
        print()
        try:
            relpos = grid[pos:pos + 16].index("+")
        except:
            relpos = grid[pos:].index("|")
        donedot = pos + relpos - 24
        gridrow = grid[donedot:donedot + 26]
        dotsinrow = []
        while len(dotsinrow) == 0:
            for i in gridrow:
                if i == dot:
                    dotsinrow.append(donedot)
                donedot += 1
            if len(dotsinrow) == 0:
                if player == Blue:
                    donedot += 0
                else:
                    donedot -= 52
                gridrow = grid[donedot:donedot + 26]
                if "a" in gridrow:
                    player = pl[pl.index(player) - 1]
                    if player == Blue:
                        pn = "Blue"
                    else:
                        pn = "Red"
                    print(gameend % (player + pn + R))
                    bfcount = len(bf)
                    rfcount = len(rf)
                    if bfcount == rfcount:
                        print(draw % (Blue + str(bfcount) + R,Red + str(rfcount) + R,player + pn + R))
                    else:
                        if bfcount > rfcount:
                            print(winner % (Blue + str(bfcount) + R,Red + str(rfcount) + R,Blue + blue + R))
                        else:
                            print(winner % (Blue + str(bfcount) + R,Red + str(rfcount) + R,Red + red + R))
                    exit()
        optionslist = []
        if move != "mov":
            for i in dotsinrow:
                if (i-2) % 26 == 0:
                    optionslist.append("a")
                elif (i-4) % 26 == 0:
                    optionslist.append("b")
                elif (i-6) % 26 == 0:
                    optionslist.append("c")
                elif (i-8) % 26 == 0:
                    optionslist.append("d")
                elif (i-10) % 26 == 0:
                    optionslist.append("e")
                elif (i-12) % 26 == 0:
                    optionslist.append("f")
                elif (i-14) % 26 == 0:
                    optionslist.append("g")
                elif (i-16) % 26 == 0:
                    optionslist.append("h")
                elif (i-18) % 26 == 0:
                    optionslist.append("i")
                elif (i-20) % 26 == 0:
                    optionslist.append("j")
                elif (i-22) % 26 == 0:
                    optionslist.append("k")
            grid[pos] = col + f + R
            prep = "Y"
            while prep == "Y":
                print(freekicklist1)
                for i in optionslist:
                    print(col + i + " " + R, end = "")
                print()
                prepos = input(freekicklist2)
                if prepos in exitlist:
                    exit()
                elif prepos.lower() in optionslist:
                    if prepos.lower() == "a":
                        pos = donedot-24
                    elif prepos.lower() == "b":
                        pos = donedot-22
                    elif prepos.lower() == "c":
                        pos = donedot-20
                    elif prepos.lower() == "d":
                        pos = donedot-18
                    elif prepos.lower() == "e":
                        pos = donedot-16
                    elif prepos.lower() == "f":
                        pos = donedot-14
                    elif prepos.lower() == "g":
                        pos = donedot-12
                    elif prepos.lower() == "h":
                        pos = donedot-10
                    elif prepos.lower() == "i":
                        pos = donedot-8
                    elif prepos.lower() == "j":
                        pos = donedot-6
                    elif prepos.lower() == "k":
                        pos = donedot-4
                    grid[pos] = here
                    for i in grid:
                        print(i, end = "")
                    print()
                    break
                else:
                    pass
    elif len(move.replace("/", "").replace("\\", "")) < 4:
        print(illegalmove)
    elif len(move.lower().replace("/", "").replace("\\", "").replace(" ", "")) == 3:
        if (move[0] == ml[0] or move[0] == ml[12]) and grid[pos - 2] in targets:
            aim1 = "←"
            pos1 = pos - 2
            p1 = grid[pos1]
        elif (move[0] == ml[1] or move[0] == ml[13]) and grid[pos + 2] in targets:
            aim1 = "→"
            pos1 = pos + 2
            p1 = grid[pos1]
        elif (move[0] == ml[2] or move[0] == ml[14]) and grid[pos - 26] in targets:
            aim1 = "↑"
            pos1 = pos - 26
            p1 = grid[pos1]
        elif (move[0] == ml[3] or move[0] == ml[15]) and grid[pos + 26] in targets:
            aim1 = "↓"
            pos1 = pos + 26
            p1 = grid[pos1]
        elif (move[:2] == ml[4] or move[:2] == ml[5] or move[:2] == ml[16] or move[:2] == ml[17]) and grid[pos - 28] in targets and grid[pos - 1] not in sl:
            aim1 = "↖"
            pos1 = pos - 28
            pos1a =  pos - 1
            p1 = grid[pos1]
        elif (move[:2] == ml[6] or move[:2] == ml[7] or move[:2] == ml[18] or move[:2] == ml[19]) and grid[pos + 24] in targets and grid[pos + 25] not in sl:
            aim1 = "↙"
            pos1 = pos + 24
            pos1a = pos + 25
            p1 = grid[pos1]
        elif (move[:2] == ml[8] or move[:2] == ml[9] or move[:2] == ml[20] or move[:2] == ml[21]) and grid[pos - 24] in targets and grid[pos + 1] not in sl:
            aim1 = "↗"
            pos1 = pos - 24
            pos1a = pos + 1
            p1 = grid[pos1]
        elif (move[:2] == ml[10] or move[:2] == ml[11] or move[:2] == ml[22] or move[:2] == ml[23]) and grid[pos + 28] in targets and grid[pos + 27] not in sl:
            aim1 = "↘"
            pos1 = pos + 28
            pos1a = pos + 27
            p1 = grid[pos1]
        else:
            p1 = "nok"
            pos1 = pos
        fsp = move.index(" ") + 1
        if (move[fsp] == ml[0] or move[fsp] == ml[12]) and grid[pos1 - 2] in targets:
            aim2 = "←"
            pos2 = pos1 - 2
            p2 = grid[pos2]
        elif (move[fsp] == ml[1] or move[fsp] == ml[13]) and grid[pos1 + 2] in targets:
            aim2 = "→"
            pos2 = pos1 + 2
            p2 = grid[pos2]
        elif (move[fsp] == ml[2] or move[fsp] == ml[14]) and grid[pos1 - 26] in targets:
            aim2 = "↑"
            pos2 = pos1 - 26
            p2 = grid[pos2]
        elif (move[fsp] == ml[3] or move[fsp] == ml[15]) and grid[pos1 + 26] in targets:
            aim2 = "↓"
            pos2 = pos1 + 26
            p2 = grid[pos2]
        elif (move[fsp:fsp + 2] == ml[4] or move[fsp:fsp + 2] == ml[5] or move[fsp:fsp + 2] == ml[16] or move[fsp:fsp + 2] == ml[17]) and grid[pos1 - 28] in targets and grid[pos1 - 1] not in sl:
            aim2 = "↖"
            pos2 = pos1 - 28
            pos2a = pos1 - 1
            p2 = grid[pos2]
        elif (move[fsp:fsp + 2] == ml[6] or move[fsp:fsp + 2] == ml[7] or move[fsp:fsp + 2] == ml[18] or move[fsp:fsp + 2] == ml[19]) and grid[pos1 + 24] in targets and grid[pos1 + 25] not in sl:
            aim2 = "↙"
            pos2 = pos1 + 24
            pos2a = pos1 + 25
            p2 = grid[pos2]
        elif (move[fsp:fsp + 2] == ml[8] or move[fsp:fsp + 2] == ml[9] or move[fsp:fsp + 2] == ml[20] or move[fsp:fsp + 2] == ml[21]) and grid[pos1 - 24] in targets and grid[pos1 + 1] not in sl:
            aim2 = "↗"
            pos2 = pos1 - 24
            pos2a = pos1 + 1
            p2 = grid[pos2]
        elif (move[fsp:fsp + 2] == ml[10] or move[fsp:fsp + 2] == ml[11] or move[fsp:fsp + 2] == ml[22] or move[fsp:fsp + 2] == ml[23]) and grid[pos1 + 28] in targets and grid[pos1 + 27] not in sl:
            aim2 = "↘"
            pos2 = pos1 + 28
            pos2a = pos1 + 27
            p2 = grid[pos2]
        else:
            p2 = "nok"
            pos2 = pos
        ssp = move.index(" ",fsp) + 1
        if (move[ssp] == ml[0] or move[ssp] == ml[12]) and grid[pos2 - 2] in targets:
            pos3 = pos2 - 2
            p3 = grid[pos3]
        elif (move[ssp] == ml[1] or move[ssp] == ml[13]) and grid[pos2 + 2] in targets:
            pos3 = pos2 + 2
            p3 = grid[pos3]
        elif (move[ssp] == ml[2] or move[ssp] == ml[14]) and grid[pos2 - 26] in targets:
            pos3 = pos2 - 26
            p3 = grid[pos3]
        elif (move[ssp] == ml[3] or move[ssp] == ml[15]) and grid[pos2 + 26] in targets:
            pos3 = pos2 + 26
            p3 = grid[pos3]
        elif (move[ssp:ssp + 2] == ml[4] or move[ssp:ssp + 2] == ml[5] or move[ssp:ssp + 2] == ml[16] or move[ssp:ssp + 2] == ml[17]) and grid[pos2 - 28] in targets and grid[pos2 - 1] not in sl:
            pos3 = pos2 - 28
            pos3a = pos2 - 1
            p3 = grid[pos3]
        elif (move[ssp:ssp + 2] == ml[6] or move[ssp:ssp + 2] == ml[7] or move[ssp:ssp + 2] == ml[18] or move[ssp:ssp + 2] == ml[19]) and grid[pos2 + 24] in targets and grid[pos2 + 25] not in sl:
            pos3 = pos2 + 24
            pos3a = pos2 + 25
            p3 = grid[pos3]
        elif (move[ssp:ssp + 2] == ml[8] or move[ssp:ssp + 2] == ml[9] or move[ssp:ssp + 2] == ml[20] or move[ssp:ssp + 2] == ml[21]) and grid[pos2 - 24] in targets and grid[pos2 + 1] not in sl:
            pos3 = pos2 - 24
            pos3a = pos2 + 1
            p3 = grid[pos3]
        elif (move[ssp:ssp + 2] == ml[10] or move[ssp:ssp + 2] == ml[11] or move[ssp:ssp + 2] == ml[22] or move[ssp:ssp + 2] == ml[23]) and grid[pos2 + 28] in targets and grid[pos2 + 27] not in sl:
            pos3 = pos2 + 28
            pos3a = pos2 + 27
            p3 = grid[pos3]
        else:
            p3 = "nok"
            pos3 = pos
        if p1 == "nok" or p2 == "nok" or p3 == "nok":
            print(occupied)
        elif pos1 == pos3 or pos1 == pos2 or pos2 == pos3:
            print(owntrail)
        else:
            grid[pos] = player + x + R
            grid[pos1] = player + aim1 + R
            try:
                grid[pos1a] = player + a + R
                pos1a = ""
            except:
                pass
            grid[pos2] = player + aim2 + R
            try:
                grid[pos2a] = player + a + R
                pos2a = ""
            except:
                pass
            grid[pos3] = here
            try:
                grid[pos3a] = player + a + R
                pos3a = ""
            except:
                pass
            pos = pos3
            player = pl[pl.index(player) - 1]
        print()
        for i in grid:
            print(i, end = "")
        print()
        if here in [grid[28],grid[30],grid[32],grid[34], grid[36], grid[38], grid[40], grid[42], grid[44], grid[46], grid[48], grid[392], grid[394], grid[396], grid[398], grid[400], grid[402], grid[404], grid[406], grid[408], grid[410], grid[412]]:
            player = pl[pl.index(player) - 1]
            if player == Blue:
                pn = "Blue"
            else:
                pn = "Red"
            print(gameend % (player + pn + R))
            bfcount = len(bf)
            rfcount = len(rf)
            if bfcount == rfcount:
                print(draw % (Blue + str(bfcount) + R,Red + str(rfcount) + R,player + pn + R))
            else:
                if bfcount > rfcount:
                    print(winner % (Blue + str(bfcount) + R,Red + str(rfcount) + R,Blue + blue + R))
                else:
                    print(winner % (Blue + str(bfcount) + R,Red + str(rfcount) + R,Red + red + R))
            player = "none"
    else:
        print(illegalmove)
