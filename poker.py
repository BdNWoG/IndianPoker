import random

players = int(input("Number of Players: "))
stack = int(input("Initial Stack: "))
BB = int(input("Big blind: "))
SB = BB/2

stacks = []
suits = ["S", "H", "C", "D"]
cards = {"A": 1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10, "J":11, "Q":12, "K":13}
deck = []
board = []
hands = []
number = 1
pot = 0

for suit in suits:
    for card in cards:
        deck.append(card + suit)
deckCopy = deck

for i in range(0, players):
    stacks.append(stack)

def endRound(deck, deckCopy):
    deck = deckCopy
    random.shuffle(deck)

def playerPreflop(deck, BB, stacks, number, hands):
    input(f"Player {number} action")
    print(f"Your stack is {stacks[number]}")
    hands.append([deck[0], deck[1]])
    deck.remove(deck[0])
    deck.remove(deck[1])
    print(f"Your cards are {hands[number - 1][0]} and {hands[number - 1][1]}")
    #call should be an action if there is bet
    try:
        action = int(input("1 Check, 2 Bet, 3 Fold: "))
    except (ValueError or action < 1 or action > 3):
        print("Invalid input")
    if (action == 1):
        return
    elif (action == 2):
        #need to define valid bet
        try:
            bet = int(input("Bet size: "))
        except (ValueError or bet > stacks[number] or bet < BB*2):
            print("Invalid bet")
    elif (action == 3):
        hands.remove(hands[number-1])
    
endRound(deck, deckCopy)
while (number <= players):
    #need to count positions still
    #need to do reraising logic
    playerPreflop(deck, BB, stacks, number, hands)
    number += 1
number = 1