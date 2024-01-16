import random

class IndianPoker:
    def __init__(self):
        self.stack = int(input("Initial Stack: "))
        self.BB = int(input("Big blind: "))
        self.SB = BB/2
        self.stacks = []
        self.suits = ["S", "H", "C", "D"]
        self.cards = {"A": 1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "T":10, "J":11, "Q":12, "K":13}
        self.deck = []
        self.hands = ["", ""]
        self.bets = [0, 0]
        self.win = 0
        self.turn = 1
        self.blind = 1

    def notPlayer(self, play):
        if self.play == 1:
            return 2
        elif self.play == 2:
            return 1

    def deckCreate(self, suits, deck, cards):
        for suit in self.suits:
            for card in self.cards:
                self.deck.append(card + suit)

    def giveStack(self, stacks, stack):
        for i in range(0, 2):
            self.stacks.append(stack)

    def endRound(self, deck, deckCopy, blind):
        self.blind = self.notPlayer(blind)
        self.deck = self.deckCopy
        self.random.shuffle(self.deck)

    def dealCards(self, hands, deck):
        self.hands[0] = self.deck[0]
        self.hands[1] = self.deck[1]
        print(f"Player 1 stack is {stacks[0]}, Player 2 stack is {stacks[1]}.")

    def setBlinds(self, BB, SB, blind, bets):
        self.bets[blind-1] = BB
        self.bets[notPlayer(blind)-1] = SB
        self.turn = self.notPlayer(blind)

    def betting(self, bets, turn, win, cards, hands, stacks):
        notTurn = notPlayer(turn)
        run = 0
        while (bets[0] != bets[1] or run < 2):
            if turn == blind:
                position = "small blind"
            else:
                position = "big blind"
            print(f"Player {turn}, {position} action: ")
            print(f"Player {notTurn} hand is {hands[notTurn-1]}")
            action = int(input("1. Fold    2. Call    3. Raise: "))
            if action == 3:
                size = int(input("Bet size: "))
                bets[turn-1] = size
                print(f"Player {turn} bets {size}, {int(size-bets[notTurn-1])} to call")
            elif action == 2:
                print(f"Player {turn} call")
                bets[turn-1] = bets[notTurn-1]
                winEval(cards, turn, hands, bets, stacks)
            elif action == 1: 
                print(f"Player {turn} fold")
                foldEval(hands, turn, stacks)
                break
            else:
                continue
            run += 1
            turn = notTurn
            notTurn = notPlayer(turn)

    def foldEval(self, hands, turn, stacks):
        notTurn = notPlayer(turn)
        stacks[turn-1] -= int(bets[turn-1])
        stacks[notTurn-1] += int(bets[turn-1])
        if hands[turn-1][0] == 'A':
            print("Ace is folded")
            stacks[notTurn-1] += int(stacks[turn-1] / 2)
            stacks[turn-1] = int(stacks[turn-1] / 2)

    def winEval(self, cards, turn, hands, bets, stacks):
        notTurn = notPlayer(turn)
        if (cards[hands[turn-1][0]] > cards[hands[notTurn-1][0]]):
            stacks[turn-1] += int(bets[notTurn-1])
            stacks[notTurn-1] -= int(bets[notTurn-1])
        elif (cards[hands[turn-1][0]] < cards[hands[notTurn-1][0]]):
            stacks[notTurn-1] += int(bets[turn-1])
            stacks[turn-1] -= int(bets[turn-1])
        bets[turn-1] = 0
        bets[notTurn-1] = 0

    def main():
        self.deckCreate(suits, deck, cards)
        self.deckCopy = deck
        self.giveStack(stacks, stack)
        while (stacks[0] != 0 or stacks[1] != 0):
            self.dealCards(hands, deck)
            self.setBlinds(BB, SB, blind, bets)
            self.betting(bets, turn, win, cards, hands, stacks)
            self.endRound(deck, deckCopy, blind)

IndianPoker.main()