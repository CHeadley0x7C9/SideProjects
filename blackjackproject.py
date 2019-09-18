import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:
	def __init__(self,suit,rank):
		self.suit = suit
		self.rank = rank 

	def __str__(self):
		return self.rank + ' of '+ self.suit

class Deck:

	def __init__(self):
		self.deck = []
		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(suit,rank))

	def shuffle(self):
		random.shuffle(self.deck)

	def deal(self):
		#taking the first card from the deck
		single_card = self.deck[0]
		self.deck.remove(self.deck[0])
		return single_card

class Hand:
	def __init__(self):
		self.cards = []
		self.value = 0
		self.aces = 0 #counts number of aces

	def add_card(self,card):
		self.cards.append(card)
		self.value += values[card.rank]
		if card.rank =='Ace':
			self.aces += 1

	def adjust_for_aces(self):
		if self.value >21 and self.aces:
			self.value -=10 
			self.value-=1

class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):

        self.total -= self.bet

def take_bet(chips):
	while True:
		try:
			chips.bet = int(input("How many chips do you want to bet? "))
		except ValueError:
			print("Sorry a bet must be an integer.")
		else:
			if chips.bet > chips.total:
				print("Sorry You don't have enough chips to bet!")
			else:
				break

def hit (deck,hand):
	hand.add_card(deck.deal())
	hand.adjust_for_aces()


def hit_or_stand(deck,hand):
	global playing
	while True: 
		x = input("Hit or Stand? Enter 'h' or 's' ")
		if x[0].lower() == 'h':
			hit(deck,hand) 
		elif x[0].lower() == 's':
			print("Player stands dealer hits")
			playing = False
		else:
			print('Sorry please try again')
			continue
		break


def show_some(player,dealer):
	print("\nDealer's Hand: ")
	print("\n[card hidden]")
	print(dealer.cards[1])
	print('\n')
	print("\nPlayer's Hand: ", *player.cards, sep ='\n')

def show_all(player,dealer):
	print("\nDealer's Hand: ", *dealer.cards, sep = '\n')
	print("\nDealer's Hand = ", dealer.value)
	print('\n')
	print("\nPlayer's Hand: ", *player.cards, sep = '\n')
	print("\nPlayer's Hand = ", player.value)


def player_busts(player,dealer,chips):
	chips.lose_bet()
	print("\nSorry that's a bust!")

def dealer_busts(player,dealer,chips):
	chips.win_bet()
	print("\nDealer busts you win!")

def player_wins(player,dealer,chips):
	chips.win_bet()
	print("\nYay you won!")

def dealer_wins(player,dealer,chips):
	chips.lose_bet()
	print("\nSorry Dealer wins this round!")

def push(player,dealer,chips):
	print("\nDealer and Player tie! It's a push.")


#start game 
print('Welcome to Blackjack. Try to get close to 21, but not over! The dealer hits untul they reach 17 Aces count as 1 or 11.')
while True:
	

	#create and shuffle deck
	deck = Deck()
	deck.shuffle()

	#start the player hand and a dealer hand with two cards
	player_hand = Hand()
	player_hand.add_card(deck.deal())
	player_hand.add_card(deck.deal())

	dealer_hand = Hand()
	dealer_hand.add_card(deck.deal())
	dealer_hand.add_card(deck.deal())

	#set up player chips 
	player_chips = Chips()

	#ask player how much they want to bet
	take_bet(player_chips)

	#show cards (hide dealer's first card)

	show_some(player_hand,dealer_hand)

	while playing: 

		#ask play if they want to hit or stand 
		hit_or_stand(deck,player_hand)

		show_some(player_hand,dealer_hand)

		if player_hand.value > 21:
			player_busts(player_hand,dealer_hand,player_chips)
		elif player_hand.value == 21:
			player_wins(player_hand,dealer_hand,player_chips)
			break


	if player_hand.value <= 21:

		while dealer_hand.value < 17: 
			hit(deck,dealer_hand)

		show_all(player_hand,dealer_hand)


	if dealer_hand.value > 21:
		dealer_busts(player_hand,dealer_hand,player_chips)

	elif dealer_hand.value < player_hand.value and player_hand.value <= 21:
		player_wins(player_hand,dealer_hand,player_chips)

	elif dealer_hand.value > player_hand.value:
		dealer_wins(player_hand,dealer_hand,player_chips)
	else:
		push(player_hand,dealer_hand,player_chips)

	#chips total
	print("\nPlayer winnings  = ", player_chips.total)

	#play agian?
	new_game = input("\nWould you like to play again? y or n ")

	if new_game[0]=='y':
		playing = True
		continue
	elif new_game[0]=='n':
		print('Thanks for playing')
		break

