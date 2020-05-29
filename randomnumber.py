#!/bin/python3
#dice game


from random import seed
from random import randint

totalbets = []
randomnum = 0
rounds = int(input("how many rounds do you want to play?:"))

money1 = 100
money2 = 100
money3 = 100
money4 = 100

for i in range(rounds):
	#betting
	totalbets = []	
	randomnum = randint(1,6)	
	player1 = int(input("Player 1 what number will appear? "))

	print("Balance:", money1)
	bet1 = int(input("Player 1 how much do you bet? "))
	totalbets.append(int(bet1))
	money1 = money1 - bet1

	print("="*70)
	player2 = int(input("Player 2 what number will appear? "))

	print("Balance:",money2)
	bet2 = int(input("Player 2 how much do you bet? "))
	totalbets.append(int(bet2))
	money2 = money2 - bet2

	print("="*70)

	#player3	 = int(input("Player 3 what number will appear? "))

	#print("Balance:",money3)
	#bet3 = int(input("Player 3 how much do you bet? "))
	#totalbets.append(int(bet3))
	#money3 = money3 - bet3

	print("="*70)

	#player4 = int(input("Player 4 what number will appear? "))

	#print("Balance:",money4)
	#bet4 = int(input("Player 4 how do you bet? "))
	#totalbets.append(int(bet4))
	#money4 = money4 - bet4

	print("="*70)


	#randomnumber
	pot = sum(totalbets)
	print("The pot is:",pot)
	print("The number is:",randomnum)
	print("="*70)
	
	
	if player1 == randomnum:
		money1 += pot
		print("player 1 wins:",pot,"!!!")
	if player2 == randomnum:
		money2 += pot
		print("player 2 wins:",pot,"!!!")
	#if player3 == randomnum:
		#money3 += pot
		#print("player 3 wins:",pot,"!!!")
	#if player4 == randomnum:
		#money4 += pot
		#print("player 4 wins:",pot,"!!!")
	

	print("="*70)
	print("SCORE:")
	print("player 1:",money1)
	print("player 2:",money2)
	#print("player 3:",money3)
	#print("player 4:",money4)
	print("="*70)

		



