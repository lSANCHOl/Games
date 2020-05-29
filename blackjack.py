#!bin/python3
import sys
import random
facevalue = [11, 10, 10, 10, 10 ,9, 8, 7, 6, 5, 4, 3, 2]
number = ["Ace", "King", "Queen", "Jack", 10, 9, 8, 7, 6, 5, 4, 3, 2]
suits = ["Spades", "Clubs", "Diamonds", "Hearts"]

money = 100

def playercard(number,suits):			
	global money
	global split	
	print("your balance:",money)	
	global hand	
	global total
	global bet
	restart = ""
	if money == 0:
		restart = input("you have no money, restart? [y/n]")
	if restart == "y":
		os.execl(sys.executable, sys.executable, *sys.argv)
	elif restart == "n":
		sys.exit()	
	
	bet = int(input("how much do you want to bet"))
	money = money - bet
	print("you now have:",money)
	print("="*70)
	hand = []	
	randomnumber = random.randint(0,12)
	randomsuit = random.randint(0,3)
	total1 = (facevalue[randomnumber])	
	card1 = (number[randomnumber]),(suits[randomsuit])
	hand.append(card1)
	
	randomnumber = random.randint(0,12)
	randomsuit = random.randint(0,3)
	total2 = (facevalue[randomnumber])	
	card2 = (number[randomnumber]),(suits[randomsuit])
	hand.append(card2)
	
	print("your hand is:",hand)
	total = total1 + total2
	print("="*70)
	#split = ""	
	#if total1 == total2:
	#	split = input("do you want to split your hand")
	#if split == "yes":
	#	splithand()
	#if split == "no":
	#	0
		


	while total < 21:
		hit = input("hit or stand?:")
		

		if hit == "hit":
			randomnumber = random.randint(0,12)
			randomsuit = random.randint(0,3)
			total3 = (facevalue[randomnumber])	
			card3 = (number[randomnumber]),(suits[randomsuit])
			total = total + total3			
			print("you got:",card3)		
			hand.append(card3)
			print("your hand is:", hand)
		
		if hit == "stand":	
			print("your hand is:", hand)
			break

	if total == 21:
		print("BLACKJACK!!!")	
	if total > 21:
		print("BUST!!!")
	print("="*70)

def dealercards(number,suits):	
	global dealerhand
	global dtotal
	dealerhand = []	
	randomnumber = random.randint(0,12)
	randomsuit = random.randint(0,3)
	dtotal1 = (facevalue[randomnumber])	
	dcard1 = ((number[randomnumber]),(suits[randomsuit]))
	print("Dealer's first card:",dcard1)	
	dealerhand.append(dcard1)
	
	randomnumber = random.randint(0,12)
	randomsuit = random.randint(0,3)
	dtotal2 = (facevalue[randomnumber])	
	dcard2 = ((number[randomnumber]),(suits[randomsuit]))
	dealerhand.append(dcard2)
	
	dtotal = dtotal1 + dtotal2
	while dtotal < 17:
		randomnumber = random.randint(0,12)
		randomsuit = random.randint(0,3)
		dtotal3 = (facevalue[randomnumber])	
		dcard3 = ((number[randomnumber]),(suits[randomsuit]))	
		dealerhand.append(dcard3)
		dtotal = dtotal + dtotal3		
		if dtotal > 21:
			print("Dealer Bust")
		
	print("="*70)
def result():
	global bet	
	global money	
	print(money)	
	print("Your hand:",hand)
	print("Dealer's hand",dealerhand)	
	print("="*70)
	if total > 21:
		if dtotal > 21:
			print("NOONE WINS!!!")
			again()	
	if dtotal == total:
		print("IT'S A DRAW!!!")
		money = money + bet
		again()	
	if dtotal == 21:
		print("Dealer wins with blackjack")
		again()	
		
	if dtotal > 21:
		bet = bet * 2		
		money = money + bet
		print("YOU WON:",bet)
		again()
	if total > 21:
		print("DEALER WINS!!!")	
		again()
	if total > dtotal:
		bet = bet * 2		
		money = money + bet
		print("YOU WON:", bet)		
		again()
	if total < dtotal:
		print("DEALER WINS!!!")
		again()
def again():
	again1 = input("Continue? [y/n]:")
	if again1 == "y":
		print("="*70)		
		playercard(number,suits)
		dealercards(number,suits)
		result()
		again()
	if again1 == "n":
		sys.exit()


def splithand():
	global handsplit
	global hand1
	global hand2
	hand1 = []
	hand2 = []
	hand1.append(hand[0])
	hand2.append(hand[1])
	print(hand1)
	print(hand2)
	
	

playercard(number,suits)
dealercards(number,suits)
result()
again()


