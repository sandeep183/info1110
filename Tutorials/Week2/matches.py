# Week 2 - Tutorial 2: Variables, Types and Formatting
# Info1110 - Sandeep S
# 13/05/2018
# matches.py A program to calculate the total number of sts a tennis player
# has won

print("Please enter <player1> <player2> <scores>")

information = input()

player1, player2, game1, game2, game3, game4, game5 = information.split(" ")

game1_player1, game1_player2 = game1.split("-")
game2_player1, game2_player2 = game2.split("-")
game3_player1, game3_player2 = game3.split("-")
game4_player1, game4_player2 = game4.split("-")
game5_player1, game5_player2 = game5.split("-")

total_games_p1 = int(game1_player1) + int(game2_player1) + int(game3_player1) + int(game4_player1) + int(game5_player1)
total_games_p2 = int(game1_player2) + int(game2_player2) + int(game3_player2) + int(game4_player2) + int(game5_player2)

total_sets_p1 = 0
total_sets_p2 = 0

if int(game1_player1) > int(game1_player2):
	total_sets_p1 += 1
else:
	total_sets_p2 += 1
	
if int(game2_player1) > int(game2_player2):
	total_sets_p1 += 1
else:
	total_sets_p2 += 1
	
if int(game3_player1) > int(game3_player2):
	total_sets_p1 += 1
else:
	total_sets_p2 += 1
	
if int(game4_player1) > int(game4_player2):
	total_sets_p1 += 1
else:
	total_sets_p2 += 1
	
if int(game5_player1) > int(game5_player2):
	total_sets_p1 += 1
else:
	total_sets_p2 += 1	
	
	
	
print("{} won {} sets and {} games".format(player1, total_sets_p1, total_games_p1))
print("{} won {} sets and {} games".format(player2, total_sets_p2, total_games_p2))


