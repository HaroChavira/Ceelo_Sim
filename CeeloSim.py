from random import randint                                    #imports randint fucntion
import time
import matplotlib.pyplot as plt
import numpy as np
import statistics
from collections import Counter

wait = 0       #sets variable to control wait times 

rounds = 0                #counts number of rounds 

rounds2play = 50000            #controls how many rounds the simulation will play

sizes = 20                        #sets size for dots in the scatter plot

mu = 4                #defines musashi values
sa = 5
shi = 6

ichi = 1
ni = 2
go = 3

bonus = 13           #sets musashi bonus
neg_bonus = -1      #sets 1-2-3 roll value
trips_bonus = 6     #sets trips bonus

message = "\033[1;30;46mMusashi!!! 13 points!!"                   #musahsi bonus message

message2 = "\033[3;30;41m3-2-1!!! -1 points!!"                  #3-2-1 rule message

draw = "\033[5;30;47mDraw"                                                     #sets draw message (the ANSI is set incorrectly so it does nothing, might want to implement it later)

total_wins_one = 0                                                            #sets variables to count number of wins for each player
total_wins_two = 0
total_wins_three = 0
total_wins_four = 0

win_mess_one = "Total wins for Player 1: "                                    #saves text to be displayed with total wins
win_mess_two = "Total wins for Player 2: "
win_mess_three = "Total wins for Player 3: "
win_mess_four = "Total wins for Player 4: "

win_list_one = []                                                             #creates empty lists in which records of scores are kept
win_list_two = []
win_list_three = []
win_list_four = []

round_counter = []

for x in range(rounds2play):                                                               #defines number of games simulated
  score1 = 0            #sets scores
  score2 = 0
  score3 = 0
  score4 = 0
  
  winners = 0                   #variable to keep count of the amount of equal highest scores
  
  
  
  print("\033[0;30;46m===Player 1 turn===")
  
  time.sleep(wait)
  
  def roll1():                                                  #deifnes dice roll for player 1
    global score1
    score1 = 0
  
    d1 = randint(1,6)                           #rolls the dice
    d2 = randint(1,6) 
    d3 = randint(1,6)           
  
    print("Three dice rolled: {} {} {}".format(d1, d2, d3))
  
    
    if d1 == d2:                                                #checks if two dice have the same value
     score1 = d3                                                #then sets the score to the die remaining
     
    if d2 == d3:
     score1 = d1
     
    if d3 == d1:
     score1 = d2
    
    if d1 == d2 and d2 ==d3:                                    #checks if all dice are equal and adds bonus points for trips (+10 points)
      score1 = d1 + trips_bonus
      
    if d1 == mu and d2 == sa and d3 == shi:                           #checks for musashi bonus
      score1 = bonus
      print(message)
      
    if d1 == mu and d2 == shi and d3 ==sa:
      score1 = bonus 
      print(message)
      
    if d1 == shi and d2 == sa and d3 == mu:
      score1 = bonus
      print(message)
      
    if d1 == shi and d2 == mu and d3 == sa:
      score1 = bonus  
      print(message)
      
    if d1 == sa and d2 == shi and d3 == mu:
      score1 = bonus  
      print(message)
      
    if d1 == sa and d2 == mu and d3 == shi:
      score1 = bonus 
      print(message)
     
    
    
    if d1 == ichi and d2 == ni and d3 == go:                          #checks for 1-2-3 rule
      score1 = neg_bonus
      print(message2)
      
    if d1 == ichi and d2 == go and d3 ==ni:
      score1 = neg_bonus 
      print(message2)
      
    if d1 == ni and d2 == go and d3 == ichi:
      score1 = neg_bonus
      print(message2)
      
    if d1 == ni and d2 == ichi and d3 == go:
      score1 = neg_bonus  
      print(message2)
      
    if d1 == go and d2 == ichi and d3 == ni:
      score1 = neg_bonus  
      print(message2)
      
    if d1 == go and d2 == ni and d3 == ichi:
      score1 = neg_bonus 
      print(message2)
                                                              
     
     
    if score1 > 0:                                              #prints players score if score is greater than zero
     print("\033[0;30;43mPlayer 1 score: {}".format(score1))
  
    time.sleep(wait)                                             #pauses for suspense
  
  for i in range(3):                                             #rolls dice again up to two more times if score is zero up until a point is scored (3 turns)
   if score1 == 0:
    roll1()
    
  if score1 ==0:                                                 #prints players score if score is zer0 (sepereated so text highlight color works properly)
    print("\033[0;30;43mPlayer 2 score: 0")    
  
  win_list_one.append(score1)
  
  #-------------------------------------------------------------------------------------------
  print("")
  print("\033[0;30;45m===Player 2 turn===")
  
  time.sleep(wait)
  
  
  def roll2():                                                    #defines dice roll fro player 2
    global score2
    score2 = 0
  
    d1 = randint(1,6)                                              #rolls the dice
    d2 = randint(1,6) 
    d3 = randint(1,6) 
    
    print("Three dice rolled: {} {} {}".format(d1, d2, d3))
  
    if d1 == d2:                                                  #checks if two dice have the same value
     score2 = d3                                                  #then sets the score to the die remaining
     
    if d2 == d3:
     score2 = d1
     
    if d3 == d1:
     score2 = d2
     
    if d1 == d2 and d2 ==d3:                                       #checks if all dice are equal and adds bonus points for trips (+10 points)
      score2 = d1 + trips_bonus  
      
    if d1 == mu and d2 == sa and d3 == shi:                        #checks for musashi bonus
      score2 = bonus
      print(message)
      
    if d1 == mu and d2 == shi and d3 ==sa:
      score2 = bonus  
      print(message)
      
    if d1 == shi and d2 == sa and d3 == mu:
       score2 = bonus  
       print(message)
      
    if d1 == shi and d2 == mu and d3 == sa:
         score2 = bonus  
         print(message)
      
    if d1 == sa and d2 == shi and d3 == mu:
      score2 = bonus  
      print(message)
      
    if d1 == sa and d2 == mu and d3 == shi:
      score2 = bonus   
      print(message)
      
      
      
    if d1 == ichi and d2 == ni and d3 == go:                          #checks for 1-2-3 rule
      score2 = neg_bonus
      print(message2)
      
    if d1 == ichi and d2 == go and d3 ==ni:
      score2 = neg_bonus 
      print(message2)
      
    if d1 == ni and d2 == ichi and d3 == go:
      score2 = neg_bonus
      print(message2)
      
    if d1 == ni and d2 == go and d3 == ichi:
      score2 = neg_bonus  
      print(message2)
      
    if d1 == go and d2 == ichi and d3 == ni:
      score2 = neg_bonus  
      print(message2)
      
    if d1 == go and d2 == ni and d3 == ichi:
      score2 = neg_bonus 
      print(message2)  
    
    if score2 > 0:                                                 #prints players score if score is greater than zer0
     print("\033[0;30;43mPlayer 2 score: {}".format(score2))               
     
    
    time.sleep(wait)    #pauses for suspense
  
  for i in range(3):                                               #rolls dice again up to two more times if score is zero up until a point is scored (3 turns)
   if score2 == 0:
    roll2()
  
  if score2 ==0:                                                    #prints players score if score is zero (had to seperate for the text highlighting to work properly)
    print("\033[0;30;43mPlayer 2 score: 0")  
  
  win_list_two.append(score2)                                       #saves each rounds score to list
  
  #------------------------------------------------------------------------------------------------------------------------------------------------
  
  
  print("")
  print("\033[0;30;42m===Player 3 turn===")
  
  time.sleep(wait)
  
  
  def roll3():                                                    #defines dice roll fro player 2
    global score3
    score3 = 0
  
    d1 = randint(1,6)                                             #rolls the dice
    d2 = randint(1,6) 
    d3 = randint(1,6) 
    
    print("Three dice rolled: {} {} {}".format(d1, d2, d3))
  
    if d1 == d2:                                                  #checks if two dice have the same value
     score3 = d3                                                  #then sets the score to the die remaining
     
    if d2 == d3:
     score3 = d1
     
    if d3 == d1:
     score3 = d2
     
    if d1 == d2 and d2 ==d3:                                       #checks if all dice are equal and adds bonus points for trips (+10 points)
      score3 = d1 + trips_bonus 
      
    if d1 == mu and d2 == sa and d3 == shi:                        #checks for musashi bonus
      score3 = bonus
      print(message)
      
    if d1 == mu and d2 == shi and d3 ==sa:
      score3 = bonus  
      print(message)
      
    if d1 == shi and d2 == sa and d3 == mu:
       score3 = bonus  
       print(message)
      
    if d1 == shi and d2 == mu and d3 == sa:
         score3 = bonus  
         print(message)
      
    if d1 == sa and d2 == shi and d3 == mu:
      score3 = bonus  
      print(message)
      
    if d1 == sa and d2 == mu and d3 == shi:
      score3 = bonus   
      print(message)
      
      
    if d1 == ichi and d2 == ni and d3 == go:                          #checks for 1-2-3 rule
      score3 = neg_bonus
      print(message2)
      
    if d1 == ichi and d2 == go and d3 ==ni:
      score3 = neg_bonus 
      print(message2)
      
    if d1 == ni and d2 == ichi and d3 == go:
      score3 = neg_bonus
      print(message2)
      
    if d1 == ni and d2 == go and d3 == ichi:
      score3 = neg_bonus  
      print(message2)
      
    if d1 == go and d2 == ichi and d3 == ni:
      score3 = neg_bonus  
      print(message2)
      
    if d1 == go and d2 == ni and d3 == ichi:
      score3 = neg_bonus 
      print(message2)  
      
    
    if score3 > 0:                                                 #prints players score if score is greater than zer0
     print("\033[0;30;43mPlayer 3 score: {}".format(score3))               
     
    
    time.sleep(wait)    #pauses for suspense
  
  for i in range(3):                                               #rolls dice again up to two more times if score is zero up until a point is scored (3 turns)
   if score3 == 0:
    roll3()
  
  if score3 ==0:                                                    #prints players score if score is zero (had to seperate for the text highlighting to work properly)
    print("\033[0;30;43mPlayer 3 score: 0")  
  
  win_list_three.append(score3)                                     #saves each rounds score to list
  
  #------------------------------------------------------------------------------------------------------------------------------------------------
  
  
  
  
  print("")
  print("\033[0;30;44m===Player 4 turn===")
  
  time.sleep(wait)
  
  
  def roll4():                                                    #defines dice roll fro player 2
    global score4
    score4 = 0
  
    d1 = randint(1,6)                                          #rolls the dice
    d2 = randint(1,6) 
    d3 = randint(1,6) 
    
    print("Three dice rolled: {} {} {}".format(d1, d2, d3))
  
    if d1 == d2:                                                  #checks if two dice have the same value
     score4 = d3                                                  #then sets the score to the die remaining
     
    if d2 == d3:
     score4 = d1
     
    if d3 == d1:
     score4 = d2
     
    if d1 == d2 and d2 ==d3:                                       #checks if all dice are equal and adds bonus points for trips (+10 points)
      score4 = d1 + trips_bonus 
      
    if d1 == mu and d2 == sa and d3 == shi:                        #checks for musashi bonus
      score4 = bonus
      print(message)
      
    if d1 == mu and d2 == shi and d3 ==sa:
      score4 = bonus  
      print(message)
      
    if d1 == shi and d2 == sa and d3 == mu:
       score4 = bonus  
       print(message)
      
    if d1 == shi and d2 == mu and d3 == sa:
         score4 = bonus  
         print(message)
      
    if d1 == sa and d2 == shi and d3 == mu:
      score4 = bonus  
      print(message)
      
    if d1 == sa and d2 == mu and d3 == shi:
      score4 = bonus   
      print(message)
      
    
    global score1
    if d1 == ichi and d2 == ni and d3 == go:                          #checks for 1-2-3 rule
      score1 = neg_bonus
      print(message2)
      
    if d1 == ichi and d2 == go and d3 ==ni:
      score4 = neg_bonus 
      print(message2)
      
    if d1 == ni and d2 == go and d3 == ichi:
      score4 = neg_bonus
      print(message2)
      
    if d1 == ni and d2 == ichi and d3 == go:
      score4 = neg_bonus  
      print(message2)
      
    if d1 == go and d2 == ichi and d3 == ni:
      score4 = neg_bonus  
      print(message2)
      
    if d1 == go and d2 == ni and d3 == ichi:
      score4 = neg_bonus 
      print(message2)  
    
    if score4 > 0:                                                 #prints players score if score is greater than zer0
     print("\033[0;30;43mPlayer 4 score: {}".format(score4))               
     
    
    time.sleep(wait)    #pauses for suspense
  
  for i in range(3):                                               #rolls dice again up to two more times if score is zero up until a point is scored (3 turns)
   if score4 == 0:
    roll4()
  
  if score4 == 0:                                                    #prints players score if score is zero (had to seperate for the text highlighting to work properly)
    print("\033[0;30;43mPlayer 3 score: 0")  
  
  win_list_four.append(score4)                                     #saves each rounds score to list
  
  
  #------------------------------------------------------------------------------------------------------------------------------------------------
  
  print("\033[0;30;0m")
  print("")
  
  list1 = [score1, score2, score3, score4]            #create a list of the scores
  
  list1.sort()                                        #sorts the list of scores
  
  if score1 == list1[-1]:   
   print("\033[5;30;47mPlayer 1 wins!!!")
   winners = winners + 1
   total_wins_one = total_wins_one + 1
  
  if score2 == list1[-1]:     
   print("\033[5;30;47mPlayer 2 wins!!!")
   winners = winners + 1
   total_wins_two = total_wins_two + 1
   
  if score3 == list1[-1]:     
   print("\033[5;30;47mPlayer 3 wins!!!")
   winners = winners + 1
   total_wins_three = total_wins_three + 1
   
  if score4 == list1[-1]:     
   print("\033[5;30;47mPlayer 4 wins!!!") 
   winners = winners +1
   total_wins_four = total_wins_four + 1
   
   
  if winners == 2:
    print("")
    print(draw)
  
  if winners == 3:
    print("")
    print(draw)
    
  if winners == 4:
    print("")
    print(draw)
    
  rounds = rounds + 1                              #counts number of rounds
  round_counter.append(rounds)                     #adds current round number to list for graph


p1sum = sum(win_list_one)                           #adds all players scores together individually
p2sum = sum(win_list_two)
p3sum = sum(win_list_three)
p4sum = sum(win_list_four)

p1mean = p1sum / rounds                              #finds the mean of each player's score
p2mean = p2sum / rounds
p3mean = p3sum / rounds
p4mean = p4sum / rounds


median1 = statistics.median(win_list_one)              #finds the mean of player scores and assigns a variable to the value
median2 = statistics.median(win_list_two)
median3 = statistics.median(win_list_three)
median4 = statistics.median(win_list_four)

mode1 = statistics.mode(win_list_one)               #finds the mode of each score set and asigns a variable to it
mode2 = statistics.mode(win_list_two)
mode3 = statistics.mode(win_list_three)
mode4 = statistics.mode(win_list_four)

dict_one = Counter(win_list_one)                    #Counts the occurences of each score for each player
dict_two = Counter(win_list_two)
dict_three = Counter(win_list_three)
dict_four = Counter(win_list_four)

score_of_neg_one = dict_one[-1] + dict_two[-1] + dict_three[-1] + dict_four[-1]          #Adds the occurences of each score for each player     
score_of_zero = dict_one[0] + dict_two[0] + dict_three[0] + dict_four[0]     
score_of_one = dict_one[1] + dict_two[1] + dict_three[1] + dict_four[1]
score_of_two = dict_one[2] + dict_two[2] + dict_three[2] + dict_four[2]      
score_of_three = dict_one[3] + dict_two[3] + dict_three[3] + dict_four[3] 
score_of_four = dict_one[4] + dict_two[4] + dict_three[4] + dict_four[4]      
score_of_five = dict_one[5] + dict_two[5] + dict_three[5] + dict_four[5]
score_of_six = dict_one[6] + dict_two[6] + dict_three[6] + dict_four[6]      
score_of_seven = dict_one[7] + dict_two[7] + dict_three[7] + dict_four[7]
score_of_eight = dict_one[8] + dict_two[8] + dict_three[8] + dict_four[8]     
score_of_nine = dict_one[9] + dict_two[9] + dict_three[9] + dict_four[9] 
score_of_ten = dict_one[10] + dict_two[10] + dict_three[10] + dict_four[10]      
score_of_eleven = dict_one[11] + dict_two[11] + dict_three[11] + dict_four[11]
score_of_twelve = dict_one[12] + dict_two[12] + dict_three[12] + dict_four[12]
score_of_thirteen = dict_one[13] + dict_two[13] + dict_three[13] + dict_four[13]

perc_neg_one = round(score_of_neg_one / (rounds2play * 4) * 100, 2)                         #finds the percentage of each score appearing
perc_zero = round(score_of_zero / (rounds2play * 4) * 100, 2)
perc_one = round(score_of_one / (rounds2play * 4) * 100, 2)
perc_two = round(score_of_two / (rounds2play * 4) * 100, 2)
perc_three = round(score_of_three / (rounds2play * 4) * 100, 2)
perc_four = round(score_of_four / (rounds2play * 4) * 100, 2)
perc_five = round(score_of_five / (rounds2play * 4) * 100, 2)
perc_six = round(score_of_six / (rounds2play * 4) * 100, 2)
perc_seven = round(score_of_seven / (rounds2play * 4) * 100, 2)
perc_eight = round(score_of_eight / (rounds2play * 4) * 100, 2)
perc_nine = round(score_of_nine / (rounds2play * 4) * 100, 2)
perc_ten = round(score_of_ten / (rounds2play * 4) * 100, 2)
perc_eleven = round(score_of_eleven / (rounds2play * 4) * 100, 2)
perc_twelve = round(score_of_twelve / (rounds2play * 4) * 100, 2)
perc_thirteen = round(score_of_thirteen / (rounds2play * 4) * 100, 2)

print("\033[0;30;47m")
print("")
print("Rounds played: ", rounds)
print("")
print(win_mess_one, total_wins_one)                #displays total number of wins for each player
print(win_mess_two, total_wins_two)
print(win_mess_three, total_wins_three)
print(win_mess_four, total_wins_four)    
print("")
#print("")
#print("Player 1 score list: ", win_list_one)             #displays a list of each player's scores (really long)
#print("Player 2 score list: ", win_list_two)
#print("Player 3 score list: ", win_list_three)
#print("Player 4 score list: ", win_list_four)
#print("")
print("Player 1 score mean: ", p1mean)                    #diplays mean of each players wins
print("Player 2 score mean: ", p2mean)
print("Player 3 score mean: ", p3mean)
print("Player 4 score mean: ", p4mean)
print("")
print("Player 1 score median: ", median1)
print("Player 2 score median: ", median2)
print("Player 3 score median: ", median3)
print("Player 4 score median: ", median4)
print("")
print("Player 1 score mode: ", mode1)
print("Player 2 score mode: ", mode2)
print("Player 3 score mode: ", mode3)
print("Player 4 score mode: ", mode4)
print("")                                   
print("Scores of -1:", score_of_neg_one, "   	   Percentage:", perc_neg_one,"%")                 #displays the occurence of each score
print("Scores of 0:", score_of_zero, "   	   Percentage:", perc_zero,"%")
print("Scores of 1:", score_of_one, "    	  Percentage:", perc_one,"%")
print("Scores of 2:", score_of_two, "    	  Percentage:", perc_two,"%")
print("Scores of 3:", score_of_three, "  	    Percentage:", perc_three,"%")
print("Scores of 4:", score_of_four, "   	   Percentage:", perc_four,"%")
print("Scores of 5:", score_of_five, "   	   Percentage:", perc_five,"%")
print("Scores of 6:", score_of_six, "  	  Percentage:", perc_six,"%")
print("Scores of 7:", score_of_seven, "   	    Percentage:", perc_seven,"%")
print("Scores of 8:", score_of_eight, "   	    Percentage:", perc_eight,"%")
print("Scores of 9:", score_of_nine, "    	   Percentage:", perc_nine,"%")
print("Scores of 10:", score_of_ten, "    	  Percentage:", perc_ten,"%")
print("Scores of 11:", score_of_eleven, "   	   Percentage:", perc_eleven,"%")
print("Scores of 12:", score_of_twelve, "   	   Percentage:", perc_twelve,"%")
print("Scores of 13:", score_of_thirteen, "   	  Percentage:", perc_thirteen,"%")


labels = ['-1', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13' ]                                #creates pie chart
scores = [score_of_neg_one, score_of_zero, score_of_one, score_of_two, score_of_three, score_of_four, score_of_five, score_of_six, score_of_seven, score_of_eight, score_of_nine, score_of_ten, score_of_eleven, score_of_twelve, score_of_thirteen]

fig, ax = plt.subplots()
ax.pie(scores, labels=labels)

plt.show()
   
#todo:
  #attach score percentages to pie chart


