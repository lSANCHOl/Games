#!/bin/python3

import random
import os
import sys


def rules():
	print("Louis' Roulette Machine")	
	print("1. possible numbers 0-10")
	print("2. can't bet more than amount of chips you have")
	print("3. even numbers are always black, odd numbers are always red and 0 is green")

resume = input("press enter to start")
print("#"*70)
chips = 10
def game(chips):	
	print("="*70)	
	random_number = random.randint(0, 10)
	if chips == 0:
		restart = input("you have run out of chips. Would you like to restart?:")
		if restart == "yes":
			os.execl(sys.executable, sys.executable, *sys.argv)
		if restart == "no":
			sys.exit()		
	print("you have",chips,"chips")
	bet = int(input("how many chips do you want to bet?:"))
		

	if bet > chips:
		print("insufficient funds")
		bet = int(input("how many chips do you want to bet?:"))
	print("="*70)
	chips = chips - bet
	print("you have",chips,"left")
	colour = input("what colour do you want?:")	
	number = int(input("what number do you want?:"))
	if number == 0:
		number ="0"


	

	if random_number % 2 == 0:
		colour_result = "black"
	if random_number % 2 != 0:
		colour_result = "red"
	if random_number == 0:
		colour_result = "green"
		random_number = "0"
	print("="*70)
	print(random_number, colour_result)

	winnings1 = 0	
	
	
		
	if random_number == number:
		winnings1 = bet * 10
	if colour_result == colour:
		winnings1 = bet * 2
	while random_number == number:
		if colour_result == colour:
			winnings1 = bet * 20
			random_number = False

	
	print("you won:", winnings1)
	print("="*70)
			
	chips = chips + winnings1

	resume = input("continue?:")
	if resume == "yes":
		game(chips)
	if resume == "no":
		sys.exit()
	print("="*70)
rules()
game(chips)

resume = input("continue?:")
if resume == "yes":
	game(chips)
if resume == "no":
	
	sys.exit()

print("="*70)

