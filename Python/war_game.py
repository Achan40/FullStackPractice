# War Game Rules:

# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.

# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.

# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.

# Ignore "double" wars

# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

class Deck:

    # This is the Deck Class. This object will create a deck of cards to initiate play
    # We use this Deck list of cards to split in half and give to the players. It will use SUITE and RANKS to create the deck. 
    # It also has a method for splitting/cutting the deck in half and Shuffling the deck.
    def __init__(self):
        # Use list comprehension to create the deck
        self.allcards = [(s,r) for s in SUITE for r in RANKS]

    def shuffle(self):
        # Shuffle the deck
        shuffle(self.allcards)
    
    def split_in_half(self):
        # Return a tuple of split deck
        return (self.allcards[:26],self.allcards[26:])

    
class Hand:

    # This is the Hand class. Each player has a Hand, and can add or remove cards from that hand
    # There is an add and remove cards method here
    def __init__(self,cards):
        self.cards = cards

    def __str__(self):
        return "Contains {} cards".format(len(self.cards))

    def add(self, added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop()

class Player:
    
    # This is the Player class, which takes in a name and an instance of a Hand class object
    # The Payer can then play cards and check if they still have cards.
    def __init__(self,name,hand):
        self.name = name
        self.hand = hand

    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has placed: {}".format(self.name, drawn_card))
        print("\n")
        return drawn_card
    
    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return war_cards
        else:
            for i in range(3):
                war_cards.append(self.hand.cards.pop())
            return war_cards

    def still_has_cards(self):

        # Return true if player still has cards left
        return len(self.hand.cards) != 0


######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")

# Create new deck and split in half
d = Deck()

# Using suffle method 
d.shuffle()

# split_in_half method returns two tuples, each is a half deck
half1, half2 = d.split_in_half()

# Create Players using Player object
comp = Player("computer", Hand(half1))

name = input("What is your name?: ")
play = Player(name, Hand(half2))

# Set round count
total_rounds = 0
war_count = 0

# Game Logic
while play.still_has_cards() and comp.still_has_cards():
    total_rounds += 1
    print("Time for a new round!")
    print("Here are the current standings")
    print(play.name + " has the count: " + str(len(play.hand.cards)))
    print(comp.name + " has the count: " + str(len(comp.hand.cards)))
    print("Play a card.")
    print("\n")

    table_cards = []

    # Play Cards
    p_card = play.play_card()
    c_card = comp.play_card()

    # Add to table_cards
    table_cards.append(c_card)
    table_cards.append(p_card)

    # Checking for war
    # Index of one since we are only comparing rankings
    if c_card[1] == p_card[1]:
        war_count += 1

        print("WAR")
        print("Each player removes 3 cards 'face down' and then one card face up")
        table_cards.extend(play.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())

        # Play cards
        c_card = comp.play_card()
        p_card = play.play_card()

        # Add to table_cards
        table_cards.append(c_card)
        table_cards.append(p_card)

        # Checking for Higher Rank
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            play.hand.add(table_cards)
        else:
            comp.hand.add(table_cards)

    else:
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            print(play.name + " has the higher card, adding to hand.")
            play.hand.add(table_cards)
        else:
            print(comp.name + " has the higher card, adding to hand.")
            comp.hand.add(table_cards)

print("Game Over, number of rounds: " + str(total_rounds))
print("A war happened " + str(war_count) + " times")
print("Does the computer still have cards? ")
print(str(comp.still_has_cards()))
print("Does the player still have cards? ")
print(str(play.still_has_cards()))